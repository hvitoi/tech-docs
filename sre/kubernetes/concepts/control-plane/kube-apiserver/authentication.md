# Authentication

- Authentication is configured in the kube-apiserver
- All authentication configuration can be stored in `kubeconfig` file

- **User authentication**
  - `basic-auth-file`: Username + Password
  - `token-auth-file`: Username + Token
  - `Certificates`
  - `External Authentication Provider (LDAP)`
  - `Service Accounts`

- **Application authentication**
  - `Service Accounts`: kubectl create serviceaccount my-sa

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: kube-apiserver
  namespace: kube-system
spec:
  containers:
    - name: kube-apiserver
      image: k8s.gcr.io/kube-apiserver-amd64:v1.11.3
      command:
        - kube-apiserver
        - --authorization-mode=Node,RBAC
        - --basic-auth-file=/tmp/users/user-details.csv
      volumeMounts:
        - name: usr-details
          mountPath: /tmp/users
          readOnly: true
  volumes:
    - name: usr-details
      hostPath:
        path: /tmp/users
        type: DirectoryOrCreate
```

## basic-auth-file

- csv file with password,username,userid
- This method is deprecated is no longer supported from Kubernetes 1.19

```csv
password123,user1,u0001
password123,user2,u0002
password123,user3,u0003
```

```conf
ExecStart=/usr/local/bin/kube-apiserver \\
  ... \\
  --basic-auth-file=user-details.csv
```

```shell
curl -X GET "/api/v1/pods" -u "user:pass"
```

## token-auth-file

- csv file with token,username,userid,group

```csv
KpjCVbI7CFAHYPkByTTzRbgu,user1,u0001,group1
ApjCVbI7CFAHYPkByTTzRbgD,user2,u0002,group2
UpjCVbI7CFAHYPkByTTzRbgq,user3,u0003,group3
```

```conf
ExecStart=/usr/local/bin/kube-apiserver \\
  ... \\
  --token-auth-file=user-details.csv
```

```shell
curl -X GET "/api/v1/pods" -header "Authorization: Bearer KpjCVbI7CFAHYPkByTTzRbgu" # token auth
```
