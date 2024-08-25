# Deploy

```shell
kubectl create ns kaniko
kubectl create secret generic docker-config --from-file=config.json -n kaniko
kubectl delete -f kaniko-directory.yml

kubectl apply -f kaniko-sc.yml
kubectl apply -f kaniko-pv.yml
kubectl apply -f kaniko-pvc.yml
kubectl apply -f kaniko.yml

kubectl delete -f kaniko.yml
kubectl delete -f kaniko-pvc.yml
kubectl delete -f kaniko-pv.yml
kubectl delete -f kaniko-sc.yml
```
