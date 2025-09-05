# Pulumi

Infrastructure as Code in any programming language

- Terminology
  - `Program`: this is the template from which stacks can be created
  - `Stack`: it's an instance of the program
  - `Resource`: smallest infrastructure building block
  - `Inputs/outputs`: read or set values for your resource

## Project structure

```conf
my-project
├── Pulumi.dev.yaml # config overrides for the prod stack
├── Pulumi.prod.yaml # config overrides for the dev stack
├── Pulumi.yaml # base configuration
├── go.mod
├── go.sum
└── main.go
```

## Stacks

- A stack is a `named update target`, and a single project may have many of them
- It's usually used for managing environments (dev, prod, etc) with it's own overrides
- Each stack has a `configuration` and `update history` associated with it, stored in the workspace (~/.pulumi/workspaces)

## State

- The "current state" stores information about the last deployed infrastructure
- With the `current state`, pulumi knows what to create, change or delete in order to achieve the `desired state`
- The state is stored at `~/.pulumi/stacks/<your-project>`
