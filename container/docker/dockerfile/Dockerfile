# Pull base image. All new images are based on existing images (Usually with an OS)
FROM alpine

# Set user to performance the following commands
USER root

# Set current folder
WORKDIR /app

# RUN is executed upon building the image
# apk package manager for Alpine
RUN apk add --update redis

# Can be override with "docker container run --entrypoint echo2 myimage"
ENTRYPOINT ["echo"]

# Can be override by the argv "docker container run myimage John"
CMD ["Henry!"]

# ENV are environment variables that are accessible inside de container. Acessible with $var1 and $var2
ENV var1=Henrique var2=Joao

# Create a volume on root of the cointainer that is accessible by the host
VOLUME /data

# Copies files from the local system onto the docker image, ignoring those in .dockerignore
COPY . /opt/source-code --exclude-from=.dockerignore

# Doesn't actually map the port! Just serve as information for the developer to use -p 3000:3000
EXPOSE 3000

# Default workdir is /
WORKDIR /usr/app
