docker image build -t hvitoi/custom-node .
docker container run -it -p 8080:8080 hvitoi/custom-node sh