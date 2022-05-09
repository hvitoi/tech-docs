# Setup

- Create the app in AWS Elastic Beanstalk
  - Add an environment
    - Save environment name
    - Save app name

- Create API keys in AWS IAM
  - Get access and secret key
  
- Setup S3 AWS storage
  - Get S3 folder path to the app

- Configure travis.ci
  - Link github to the travis
  - Select the desired repository
  - Create .travis.yml with
    - Script for buildind and running test
    - Script for deploying
  - Add environment variables with the AWS access key and secret key

# Workflow
- Push to github master branch
- Travis detects new alterations in master branch
- Travis build test and run tests
- Travis copies the master branch to AWS S3 if tests are ok
- AWS builds the production Dockerfile
- AWS runs the docker image