# Git Hook

- Git Hook is a `trigger`
- E.g., whenever code is pushed to master branch, github/gitlab must trigger a script
- Git hooks must be placed at `.git/hooks` folder

## Example hook

- If some code is pushed to master branch, then get a jenkins crumb and build a job

```bash
#!/bin/bash
if ! [ -t 0 ]; then
  read -a ref
fi
IFS='/' read -ra REF <<<"${ref[2]}"
branch="{REF[2]}"

if [ $branch == "master" ]; then
  crumb=$(curl "http://localhost:8080/crumbIssuer/api/xml?xpath=concat(//crumbRequestField,':',//crumb)" -u "admin:123")
  curl -X "POST" "http://localhost:8080/job/job-name/build?delay=0sec" -u "admin:123" -H "$crumb"

  if [ $? -eq 0 ]; then
    echo "*** OK"
  else
    echo "*** Error"
  fi

fi
```
