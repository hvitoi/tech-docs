#!/bin/bash

# Get crumb
crumb=`curl -u "admin:123" -s 'http://localhost:8080/crumbIssuer/api/xml?xpath=concat(//crumbRequestField,":",//crumb)'`
echo crumb

# Invoke job (no parameters)
curl -u "admin:123" -H "$crumb" -X POST "http://localhost:8080/job/simple-job/build?delay=0sec"