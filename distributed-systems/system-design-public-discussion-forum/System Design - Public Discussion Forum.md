# Marketplace - Public Discussion Forum

## Functional Requirements

- User should be able to post questions/news
  - What does it contain? Images, text, tags?
  - Who can create and view posts?
- User should be able to comment on existing posts
  - Comment on another comment?
- User should be able to upvote/downvote posts/comments
- User should be able to see the feed with the most popular posts
  - The most popular post is the most voted?

## Non-Functional Requirements

- Scalability
  - Total Users
    - 200M customers
  - Daily access
    - 100M customers/day
  - Daily created posts
    - 10M posts/day
  - Daily comments
    - 100M comments/day
  - Daily upvote/downvote
    - 200M votes/day
  - Geographic distribution
    - Global
- Performance
  - Response time requirements (all APIs)
- Availability
  - Availability \+ Partition Tolerance (AP over CP)

## System Constraints

- Number of engineers and teams and will be working on this project
  - 20 engineers, 3 teams

## SQL

```sql
SELECT
Post\_post\_id,
SUM(votes.vote\_id) num\_of\_votes
FROM
posts
JOIN
votes
ON votes.parent\_id \= posts.post\_id
GROUP BY
post.post\_id
ORDER BY
num\_of\_votes DESC
LIMIT 10
```
