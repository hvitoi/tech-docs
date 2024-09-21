# Config

```yaml
apiVersion: skaffold/v2alpha3
kind: Config
deploy:
  kubectl:
    # There is a collection of config files in these folders
    # Anytime a change is made, it's automatically reapplied
    # Also delete the objects when skaffold is stopped
    manifests:
      - ./infra/k8s/*
build:
  # Don't automatically push to dockerhub after building an image
  local:
    push: false
  # Images to attempt to rebuild after changed
  artifacts:
    - image: hvitoi/blog-client
      context: client # This is the directory
      docker:
        dockerfile: Dockerfile # Dockerfile to build

      # Setup a manual action if the file is a .js file. If it's not, the whole image will be rebuilt
      sync:
        manual:
          - src: 'src/**/*.js' # Take the file and directly throw into the pod
            dest: . # Destination inside of the pod (auth directory)

    - image: hvitoi/blog-posts
      context: posts
      docker:
        dockerfile: Dockerfile
      sync:
        manual:
          - src: '*.js'
            dest: .

    - image: hvitoi/blog-comments
      context: comments
      docker:
        dockerfile: Dockerfile
      sync:
        manual:
          - src: '*.js'
            dest: .

    - image: hvitoi/blog-eventbus
      context: eventbus
      docker:
        dockerfile: Dockerfile
      sync:
        manual:
          - src: '*.js'
            dest: .
    - image: hvitoi/blog-moderation
      context: moderation
      docker:
        dockerfile: Dockerfile
      sync:
        manual:
          - src: '*.js'
            dest: .
    - image: hvitoi/blog-query
      context: query
      docker:
        dockerfile: Dockerfile
      sync:
        manual:
          - src: '*.js'
            dest: .
# Sometimes it might be necessary to type 'thisisunsafe' on the chrome page (anywhere)
```
