# GraphQL

- Allows responding with only the necessary data needed by the client
- It is a single entrypoint `POST /graphql`

## Type System

- Provides a type system

```gql
type Book {
  id: ID! # required
  title: String
  authors: [Author]
}

type Author {
  id: ID!
  name: String
  books: [Book]
}

# Query Type: entry-point to READ data
type Query {
  getBook(id: ID!): Book
}

# Mutation Type: entry-point to WRITE data
type Mutation {
  createVideo(url: String): Video
  deleteVideo(url: String): String
}
```

## Resolvers

- Resolvers are functions that `resolve the queries`

```javascript
export const resolvers = {
  Query: {
    creator(obj, args, context, info) {
      return context
                .db
                .getCreator(args.id)
    }
  }
}
```

## Query

```gql
query getBook(id: '123') {
  rocket {
    name
    thrust
    captain {
      name
      callsign
    }
  }
}
```

```gql
query MyQuery(
  $categorySlug: String
  $limit: Int
  $skip: Int
  $filters: QuestionListFilterInput
) {
  questionList(
    categorySlug: $categorySlug
    limit: $limit
    skip: $skip
    filters: $filters
  ) {
    data {
      likes
      acRate
      difficulty
      freqBar
      questionFrontendId
      isFavor
      paidOnly: isPaidOnly # isPaidOnly is the real name
      status
      title
      titleSlug
      topicTags {
        name
        id
        slug
      }
      hasSolution
      hasVideoSolution
    }
  }
}

```

- **Request**

```json
{
  "query": "the_query",
  "variables": {
    "a": "a",
    "b": "b",
  }
}
```

```shell
curl --request POST \
  --url https://leetcode.com/graphql/ \
  --header 'Content-Type: application/json' \
  --data '{"query":"query MyQuery(\n\t$categorySlug: String\n\t$limit: Int\n\t$filters: QuestionListFilterInput\n) {\n\tquestionList(\n\t\tcategorySlug: $categorySlug\n\t\tlimit: $limit\n\t\tfilters: $filters\n\t) {\n\t\tdata {\n\t\t\ttitleSlug\n\t\t\tlikes\n\t\t}\n\t}\n}\n","operationName":"MyQuery","variables":"{\n\t\"categorySlug\": \"all-code-essentials\",\n\t\"limit\": 1000000,\n\t\"filters\": {}\n}"}'
```

- **Response**

```json
{
  "name": "Saturn V",
  "thrust": 7891000,
  "captain": {
    "name": "Neil Armstrong",
    "callsign" :"Neil"
  }
}
```
