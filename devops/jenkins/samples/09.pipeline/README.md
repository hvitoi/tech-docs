# Jenkins pipeline example

- This workflow consists of 3 components

  - Jenkins server
  - Jenkins agent
  - Deployment machine

- The `jenkins agent` must have installed `docker` (for build image and push) and `maven` (for build java code)
- Generate the a `key-pair` and give the public key to the jenkins agent (`/config/.ssh/authorized-keys`) and the private key to the jenkins master
