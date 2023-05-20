# Microservices

## Benefits of microservices

- More options to scale up application
- Independent deployability
- Limit the "blast radius" of failure

`Microservices architectures buy you options` - James Lewis

- Industry tends to focus on tech instead of the outcome. One should use microservices as a means to obtain a desired outcome rather than for the sake of using a new technology

## Monolith as default option

- Microservices shouldn't be the default option. If you think a service architecture could help, try it with one of the modules from a very simple monolith typology and let it evolve from there

## Top 3 reasons to use microservices

1. Zero-downtime independent deployability

- SaaS business where you can't afford downtime

1. Isolation of processing around around

- Healthcare industries, GDPR
- How to know where my customer data is
- How to implement the "right to be forgotten"

1. Enable a higher degree of organization autonomy

- Distribute responsibilities into teams to reduce the amount of coordination with the rest of the organization

## How to avoid a distributed monolith

1. Create a deployment mechanism
1. Look for patterns and decide how to deal with them

- E.g., a collection of microservices being changed together
- Use Jira to tie a commit to a piece of work
- Look the stories completed and the commits
- Map the commits to the services those stories have impacted

1.
