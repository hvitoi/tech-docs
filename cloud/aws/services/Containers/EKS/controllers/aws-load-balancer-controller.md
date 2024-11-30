# aws-load-balancer-controller

> This controller is required for Ingress objects only. It creates ALB resources on AWS based on Ingress Objects
> For Service objects this controller is not required (although it can also be used). Service Objects (type LoadBalancer) support is built-in and creates CLBs or NLBs resources on AWS.

- Automatically create ALBs or NLBs based on Ingress Kubernetes Objects
  - `K8S Ingress Object` -> `AWS ALB`
  - `K8S Service Object` -> `AWS NLB`
- <https://kubernetes-sigs.github.io/aws-load-balancer-controller>
- This controller was previously named "aws-alb-ingress-controller"

## Architecture

![LB Controller](.images/lb-controller-architecture1.png)
![LB Controller](.images/lb-controller-architecture2.png)

- The target group can either be
  - 1. Each node in the cluster (instance mode)
  - 1. Each individual pod (IP mode)

> With CLB (not managed by this controller) the target group is always each pod of the app

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

## Annotations

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
  - Traffic is routed to the `NodePort` of each node
  - This requires NodePorts to be previously created

- **IP Mode**
  - `alb.ingress.kubernetes.io/target-type: ip`
  - The target group is each pod of the application
  - Register pods as targets (instead of the nodes)
  - This option is mandatory for Fargate profiles because fargate nodes do not support NodePort services

```yaml
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

### Access control

#### scheme

- `internet-facing`
- `internal`

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
    alb.ingress.kubernetes.io/ssl-policy: ELBSecurityPolicy-TLS-1-1-2017-01 # this is already the default ssl policy
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
    alb.ingress.kubernetes.io/healthcheck-protocol: HTTP
    alb.ingress.kubernetes.io/healthcheck-port: traffic-port
    alb.ingress.kubernetes.io/healthcheck-interval-seconds: "15"
    alb.ingress.kubernetes.io/healthcheck-timeout-seconds: "5"
    alb.ingress.kubernetes.io/success-codes: "200"
    alb.ingress.kubernetes.io/healthy-threshold-count: "2"
    alb.ingress.kubernetes.io/unhealthy-threshold-count: "2"
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
