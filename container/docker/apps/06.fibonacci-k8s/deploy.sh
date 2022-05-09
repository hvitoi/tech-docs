# Build images. Tag it 2 tags: latest and GIT_SHA
docker build -t hvitoi/fibo-web:latest -t hvitoi/fibo-web:$SHA -f ./web/Dockerfile ./web
docker build -t hvitoi/fibo-api:latest -t hvitoi/fibo-api:$SHA -f ./api/Dockerfile ./api
docker build -t hvitoi/fibo-worker:latest -t hvitoi/fibo-worker:$SHA -f ./worker/Dockerfile ./worker

# Push images to Docker Hub
docker push hvitoi/fibo-web:latest
docker push hvitoi/fibo-api:latest
docker push hvitoi/fibo-worker:latest
docker push hvitoi/fibo-web:$SHA
docker push hvitoi/fibo-api:$SHA
docker push hvitoi/fibo-worker:$SHA

# Apply config files
kubectl apply -f k8s

# Explicitly set a image for the deployment object
kubectl set image deployments/web-deployment web=hvitoi/fibo-web:$SHA
kubectl set image deployments/api-deployment api=hvitoi/fibo-api:$SHA
kubectl set image deployments/worker-deployment worker=hvitoi/fibo-worker:$SHA