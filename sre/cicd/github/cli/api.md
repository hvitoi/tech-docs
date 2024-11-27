# gh api

```shell
gh api --silent \
  -H "Accept: application/vnd.github+json" \
  -H "X-GitHub-Api-Version: 2022-11-28" \
  "orgs/foo/teams/my-team"

curl -Lsf \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer $token" \
  -H "X-GitHub-Api-Version: 2022-11-28" \
  https://api.github.com/orgs/foo/teams/my-team
```

## GraphQL explorer

- <https://docs.github.com/en/graphql/overview/explorer>

```graphql
query userInfo($login: String!) {
  user(login: $login) {
    name
    repositoriesContributedTo(
      first: 100
      includeUserRepositories: true
      contributionTypes: [COMMIT, ISSUE, PULL_REQUEST, REPOSITORY]
    ) {
      totalCount
      pageInfo {
        endCursor
        hasNextPage
      }
    }
    contributionsCollection(from:"2024-01-01T00:00:00.000Z", to:"2024-12-31T00:00:00.000Z") {
        commitContributionsByRepository(maxRepositories: 100) {
        repository {
          nameWithOwner,
          description
        }
        contributions {
          totalCount
        }
      }
      pullRequestContributionsByRepository(maxRepositories: 100) {
        repository {
          nameWithOwner,
          description
        }
        contributions {
          totalCount
        }
      }
      totalCommitContributions
      totalIssueContributions
      totalPullRequestContributions
      totalPullRequestReviewContributions
    }
  }
}
```

With variables

```json
{"login": "your-gh-handle"}
```
