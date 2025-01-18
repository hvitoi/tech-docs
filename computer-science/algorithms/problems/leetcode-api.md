# Leetcode API

- Fetch most liked problems

```shell
curl -s --request POST \
  --url https://leetcode.com/graphql/ \
  --header 'Content-Type: application/json' \
  --data '{
      "query": "query MyQuery { questionList(categorySlug: \"all-code-essentials\" limit: 9999 filters: {}) { data { questionFrontendId titleSlug likes difficulty topicTags { slug } } } }",
      "operationName": "MyQuery",
      "variables": {"categorySlug":"all-code-essentials","filters":{}}
  }' \
  | jq '.data.questionList.data | sort_by(.likes) | reverse | map(select(.likes > 3000))' > problems.json
```
