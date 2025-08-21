# Pull base image. All new images are based on existing images (Usually with an OS)
FROM alpine

# Set user to perform the commands
USER root

# Set current folder. Default is /
WORKDIR /app

# Commands to execute upon building the image
RUN apk add --update redis

# Environment variables to be available in the container
ENV var1=Henrique var2=Joao

# Create a volume on root of the cointainer that is accessible by the host
VOLUME /data

# Copies files from the local system onto the docker image, ignoring those in .dockerignore
COPY . /opt/source-code --exclude-from=.dockerignore

# Doesn't actually map the port! Just serve as information for the developer to use -p 3000:3000
EXPOSE 3000

# Can be override with "docker container run --entrypoint echo2 myimage"
ENTRYPOINT ["echo"]

# Can be override by the argv "docker container run myimage John"
# Exec form (recommended) - does not use a command shell
CMD ["Henry!"]
# Shell form (not recommended) - uses a command shell
CMD "Henry!"
