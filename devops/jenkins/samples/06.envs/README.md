# Environment variables in Jenkins

- Built-in environment variables available in jenkins container

```shell
echo "Build number: $BUILD_NUMBER"
echo "Build ID: $BUILD_ID"
echo "Build URL: $BUILD_URL"
echo "Job name: $JOB_NAME"
```

## Custom environment variables

- `Manage Jenkins` -> `Configure System` -> `Global properties`
