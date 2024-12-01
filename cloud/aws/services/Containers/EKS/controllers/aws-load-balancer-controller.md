# aws-load-balancer-controller

- Automatically create ALBs or NLBs
  - `K8S Ingress Object` -> `AWS ALB`
  - `K8S Service Object` -> `AWS NLB`
- <https://kubernetes-sigs.github.io/aws-load-balancer-controller>

> There is also the legacy in-tree controller (kube-controller-manager / cloud-controller-manager) built-in into Kubernetes. With this controller it is possible to create only CLBs and NLBs with basic functionality. This built-in controller is legacy and should be avoided in favor of aws-load-balancer-controller.

## Architecture

![LB Controller](.images/lb-controller-architecture1.png)
![LB Controller](.images/lb-controller-architecture2.png)

- The target group can either be
  - 1. Each node in the cluster (instance mode)
  - 1. Each individual pod (IP mode)

## Permissions

- The controller runs on the worker nodes, so it needs access to the `AWS ALB/NLB` APIs with IAM permissions
- The IAM permissions can either be setup using:
  - `Pod Identity` (preferred)
  - `IAM roles for service accounts (IRSA)`
  - Policies attached directly to the `worker node IAM roles`

### Pod Identity

- It is necessary to have the `Amazon EKS Pod Identity Agent Addon` installed in the cluster

```shell
# Download Policy
curl -O https://raw.githubusercontent.com/kubernetes-sigs/aws-load-balancer-controller/v2.10.0/docs/install/iam_policy.json

# Create IAM policy
aws iam create-policy \
  --policy-name MyAWSLoadBalancerControllerIAMPolicy \
  --policy-document file://iam_policy.json

set account_id (aws sts get-caller-identity --query Account --output text)
eksctl create podidentityassociation \
  --cluster foo \
  --namespace kube-system \
  --service-account-name aws-load-balancer-controller \
  --create-service-account \
  --permission-policy-arns arn:aws:iam::$account_id:policy/MyAWSLoadBalancerControllerIAMPolicy
```

### IRSA

- You can define the required IRSA with eksctl manifest:

```yaml
iam:
  withOIDC: true
  serviceAccounts:
    - metadata:
        name: aws-load-balancer-controller
        namespace: kube-system
      wellKnownPolicies:
        awsLoadBalancerController: true
```

- Or create it manually

```shell
# Create an OIDC provider
eksctl utils associate-iam-oidc-provider --cluster foo --approve

# Download Policy
curl -O https://raw.githubusercontent.com/kubernetes-sigs/aws-load-balancer-controller/v2.10.0/docs/install/iam_policy.json

# Create IAM policy
aws iam create-policy \
  --policy-name AWSLoadBalancerControllerIAMPolicy \
  --policy-document file://iam_policy.json

# Create IRSA
set account_id (aws sts get-caller-identity --query Account --output text)
eksctl create iamserviceaccount \
  --name aws-load-balancer-controller \
  --cluster foo \
  --namespace kube-system \
  --attach-policy-arn=arn:aws:iam::$account_id:policy/AWSLoadBalancerControllerIAMPolicy \
  --override-existing-serviceaccounts \
  --approve
```

## Installation

```shell
helm repo add eks https://aws.github.io/eks-charts
helm repo update eks
helm install aws-load-balancer-controller eks/aws-load-balancer-controller \
  --namespace kube-system \
  --set "clusterName=foo" \
  # do not create SA because it has already been created when creating the IRSA
  --set "serviceAccount.create=false" \
  # SA that was created as part of the IRSA creation
  --set "serviceAccount.name=aws-load-balancer-controller"
```

- This creates in the kube-system namespace:
  - `sa/aws-load-balancer-controller`: created as part of creating the IRSA
  - `secret/aws-load-balancer-tls`: contains the tls.key, tls.crt and ca.crt
  - `deplyo/aws-load-balancer-controller`: uses the above SA and mounts the above secret
  - `svc/eks-extension-metrics-api`: exposes port 443 (that targets port 9443 on the container)
  - `ingressclasses/alb`: IngressClass to be used by Ingress objects

## Annotations (ALB)

- <https://kubernetes-sigs.github.io/aws-load-balancer-controller/latest/guide/ingress/annotations/>

### Traffic Routing

- Name of the LB resource to be created at AWS

#### load-balancer-name

```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: my-ing
  annotations:
    alb.ingress.kubernetes.io/load-balancer-name: my-awesome-lb
spec:
  ingressClassName: my-aws-ingress-class
  defaultBackend:
    service:
      name: my-svc-nodeport
      port:
        number: 80
```

#### target-type

- Defines the Ingress Traffic
- AWS Load Balancer controller supports two traffic modes

- **Instance Mode** (default)
  - `alb.ingress.kubernetes.io/target-type: instance`
  - The target group is the NodePort of each node
  - Register the nodes (ec2 instances) as targets for the ALB
  - This requires a `Service NodePort` object to be manually created (and referenced as a backend in the Ingress Object)

- **IP Mode**
  - `alb.ingress.kubernetes.io/target-type: ip`
  - The target group is each pod of the application
  - Register pods as targets. Traffic is routed directly to the pods.
  - This requires a `Service ClusterIP` object to be manually created (and referenced as a backend in the Ingress Object)
  - IP mode is required for `sticky sessions` (when same user session needs to talk with the same pod)
  - This option is mandatory for Fargate profiles because fargate nodes do not support NodePort services
  - If the Pod IP is directly used, why is there a need for a ClusterIP? Because the ClusterIP is used by the ALB target group to know what are the Pod IPs. The ClusterIP has the information of all Pod IPs

```yaml
# INSTANCE MODE
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: my-ing
  annotations:
    alb.ingress.kubernetes.io/target-type: instance
spec:
  ingressClassName: my-aws-ingress-class
  defaultBackend:
    service:
      name: my-svc-nodeport
      port:
        number: 80
```

```yaml
# IP MODE
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: my-ing
  annotations:
    alb.ingress.kubernetes.io/target-type: ip
spec:
  ingressClassName: my-aws-ingress-class
  defaultBackend:
    service:
      name: my-svc-clusterip
      port:
        number: 80
```

### Access control

#### scheme

- **internet-facing**: to be exposed to the www
- **internal**: to be used by other aws services

```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: my-ing
  annotations:
    alb.ingress.kubernetes.io/scheme: internet-facing
spec:
  ingressClassName: my-aws-ingress-class
  defaultBackend:
    service:
      name: my-svc-nodeport
      port:
        number: 80
```

### Health Check

- If no healthcheck is defined, uses `HTTP` on `/`
- If your ingress is redirecting to multiple backends you should **NOT** define healthchecks here, but instead define it per route at the `Service` object
  - The annotations names are exactly the same when defining it at the `Service` object

```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: my-ing
  annotations:
    alb.ingress.kubernetes.io/healthcheck-protocol: HTTP
    alb.ingress.kubernetes.io/healthcheck-path: /index.html
    alb.ingress.kubernetes.io/healthcheck-port: traffic-port # "traffic-port" uses the same port as the target container
    alb.ingress.kubernetes.io/healthcheck-interval-seconds: "15"
    alb.ingress.kubernetes.io/healthcheck-timeout-seconds: "5"
    alb.ingress.kubernetes.io/success-codes: "200"
    alb.ingress.kubernetes.io/healthy-threshold-count: "2"
    alb.ingress.kubernetes.io/unhealthy-threshold-count: "2"
spec:
  ingressClassName: my-aws-ingress-class
  defaultBackend:
    service:
      name: my-svc-nodeport
      port:
        number: 80
```

### Traffic Listening

#### listen-ports

```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: my-ing
  annotations:
    alb.ingress.kubernetes.io/listen-port: '[{"HTTP":80}]' # this is already the default
spec:
  ingressClassName: my-aws-ingress-class
  defaultBackend:
    service:
      name: my-svc-nodeport
      port:
        number: 80
```

#### ssl-redirect

- Automatically redirect traffic (e.g., port 80) to port 443
- This redirect is done by the LB
- This requires the HTTPS (port 443) to be set up (see TLS section)

```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: my-ing
  annotations:
    alb.ingress.kubernetes.io/ssl-redirect: '443'
spec:
  ingressClassName: my-aws-ingress-class
  defaultBackend:
    service:
      name: my-svc-nodeport
      port:
        number: 80
```

### Ingress Groups

- Usually there is a single Ingress Manifest for all the routing rules. This manifest may get messy if you have 50 apps managed by a single ingress manifest (and a single ALB).
- With `Ingress Groups` we can create multiple Ingresses that are associated with a `single Load Balancer`
- The controller will `merge all the ingress rules` and support them in a single ALB
- The other annotations within an ingress are applied to the paths in that ingress only! (not to all paths defined in all ingresses in that group)

```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: my-ing
  annotations:
    alb.ingress.kubernetes.io/load-balancer-name: awesome-lb # the next ingress using this same ALB won't get an error (lb already exists) because it's part of an ingress group
    alb.ingress.kubernetes.io/scheme: internet-facing
    alb.ingress.kubernetes.io/group.name: myapps.web # all ingresses with this group name are associated with the same ALB
    alb.ingress.kubernetes.io/group.order: "10" # define among the ingresses within this group which has priority (if the configurations conflict with each other)
spec:
  ingressClassName: my-aws-ingress-class
  rules:
    - http:
        paths:
          - path: /app1
            pathType: Prefix
            backend:
              service:
                name: my-svc-nodeport
                port:
                  number: 80
```

### TLS

- Establishes a HTTPS connection between the client and the loadbalancer
- If your certificate is for your own domain (e.g., *.example.com), you need to add a `CNAME record` that targets your LB address or a `A record` that targets your LB IPv4. To automatically add the DNS records check `external-dns`
- The certificate arn has to be manually created at AWS beforehand! For a more automated process

```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: my-ing
  annotations:
    alb.ingress.kubernetes.io/listen-port: '[{"HTTPS":443},{"HTTP":80}]'
    alb.ingress.kubernetes.io/ssl-redirect: '443' # automatically redirect to https
    alb.ingress.kubernetes.io/certificate-arn: arn:aws:acm:us-east-1:123456789012:certificate/foo # uses this certificate for TLS encryption. To avoid having to hard-coding it here you can also use
    alb.ingress.kubernetes.io/ssl-policy: ELBSecurityPolicy-TLS-1-1-2017-01 # SSL Negotiation Policy. By default uses the latest
spec:
  ingressClassName: my-aws-ingress-class
  defaultBackend:
    service:
      name: my-svc-nodeport
      port:
        number: 80
```

- With `SSL Certificate Discovery using Host` the ingress controller will attempt to discover the `TLS certificate ARN` from the configured in `spec.tls[].hosts[]` in the Ingress Object. There is no additional annotation required for this certificate discovery (just `spec.tls[].hosts[]` by itself)

```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: my-ing
  annotations:
    alb.ingress.kubernetes.io/load-balancer-name: awesome-lb
    alb.ingress.kubernetes.io/scheme: internet-facing
    alb.ingress.kubernetes.io/listen-ports: '[{"HTTPS":443}, {"HTTP":80}]'
    alb.ingress.kubernetes.io/ssl-redirect: "443"
    external-dns.alpha.kubernetes.io/hostname: foo.hvitoi.com
spec:
  ingressClassName: my-aws-ingress-class
  defaultBackend:
    service:
      name: my-svc-nodeport
      port:
        number: 80
  rules:
    - http:
        paths:
          - path: /app1
            pathType: Prefix
            backend:
              service:
                name: my-app1-svc-nodeport
                port:
                  number: 80
    - http:
        paths:
          - path: /app2
            pathType: Prefix
            backend:
              service:
                name: my-app2-svc-nodeport
                port:
                  number: 80
    tls:
    - hosts:
        # automatically try to pick the certificate from the cloud provider (in this case it's not necessary to define the certificate-arn)
        # tries to find in the cloud a certificate with the same CN
        # The Ingress controller must have permissions to access ACM
        - "*.hvitoi.com"
```

## Annotation (NLB)

```yaml
apiVersion: v1
kind: Service
metadata:
  name: my-svc-lb
  annotations:
    # Traffic Routing
    service.beta.kubernetes.io/aws-load-balancer-name: awesome-lb
    service.beta.kubernetes.io/aws-load-balancer-type: external # this tells Kubernetes to use the aws-load-balancer-controller (and not the in-tree controller). You can also use loadBalancerClass: service.k8s.aws/nlb instead
    service.beta.kubernetes.io/aws-load-balancer-nlb-target-type: instance # instance (default) or ip
    service.beta.kubernetes.io/aws-load-balancer-subnets: subnet-xxxx, mySubnet # Subnets are auto-discovered if this annotation is not specified

     # Health Check Settings
    service.beta.kubernetes.io/aws-load-balancer-healthcheck-protocol: http
    service.beta.kubernetes.io/aws-load-balancer-healthcheck-port: traffic-port
    service.beta.kubernetes.io/aws-load-balancer-healthcheck-path: /index.html
    service.beta.kubernetes.io/aws-load-balancer-healthcheck-healthy-threshold: "3"
    service.beta.kubernetes.io/aws-load-balancer-healthcheck-unhealthy-threshold: "3"
    service.beta.kubernetes.io/aws-load-balancer-healthcheck-interval: "10" # The controller currently ignores the timeout configuration due to the limitations on the AWS NLB. The default timeout for TCP is 10s and HTTP is 6s.

    # Access Control
    service.beta.kubernetes.io/load-balancer-source-ranges: 0.0.0.0/0  # specifies the CIDRs that are allowed to access the NLB.
    service.beta.kubernetes.io/aws-load-balancer-scheme: "internet-facing" # specifies whether the NLB will be internet-facing or internal

    # AWS Resource Tags
    service.beta.kubernetes.io/aws-load-balancer-additional-resource-tags: Environment=dev,Team=test

    # TLS
    service.beta.kubernetes.io/aws-load-balancer-ssl-cert: arn:aws:acm:us-east-1:123456789012:certificate/d86de939-8ffd-410f-adce-0ce1f5be6e0d # specifies the ARN of one or more certificates managed by the AWS Certificate Manager.
    service.beta.kubernetes.io/aws-load-balancer-ssl-ports: 443, # Specify this annotation if you need both TLS and non-TLS listeners on the same load balancer
    service.beta.kubernetes.io/aws-load-balancer-ssl-negotiation-policy: ELBSecurityPolicy-TLS13-1-2-2021-06 # specifies the Security Policy for NLB frontend connections, allowing you to control the protocol and ciphers.
    service.beta.kubernetes.io/aws-load-balancer-backend-protocol: tcp # specifies whether to use TLS or TCP for the backend traffic between the load balancer and the kubernetes pods.

    # External DNS
    external-dns.alpha.kubernetes.io/hostname: nlbdns101.stacksimplify.com # For creating autormatically a Record Set (DNS Records) in Route53
spec:
  type: LoadBalancer
  loadBalancerClass: service.k8s.aws/nlb
  selector:
    app: my-app
  ports:
    - port: 80 # creates "listener" 80 in NLB
      targetPort: 80 # creates "target group" in NLB
    - port: 443
      targetPort: 80 # create a new "target group" (even though there is already a target group with port 80)
```
