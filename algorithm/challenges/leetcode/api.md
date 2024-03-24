# Leetcode API

- Fetch most liked problems

```shell
curl --request POST \
  --url https://leetcode.com/graphql/ \
  --header 'Content-Type: application/json' \
  --data '{"query":"query MyQuery {\n\tquestionList(\n\t\tcategorySlug: \"all-code-essentials\"\n\t\tlimit: 9999\n\t\tfilters: {}\n\t) {\n\t\tdata {\n\t\t\ttitleSlug\n\t\t\tlikes\n\t\t}\n\t}\n}\n","operationName":"MyQuery","variables":"{\n\t\"categorySlug\": \"all-code-essentials\",\n\t\"filters\": {}\n}"}' | jq '.data.questionList.data | sort_by(.likes) | reverse'
```
