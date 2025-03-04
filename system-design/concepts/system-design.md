# System Design

> "The software architecture of a system is a high-level description of the system's structure, its differente components, and how those components communicate with each other to fulfill the systems' requirements and constrainst"

There is a lot of ambiguity on system design, and it may be eased by well defined requirements

## Scope of the Design

> From low-level to high-level

1. `Classes`, structs
    - Organization and communications between objects inside of a program
1. `Modules`, packages, libraries
    - Similar to the latter, but for bigger codebase
1. `Services`, components, applications
    - Organization of separate components with a defined domain

Application > Library > Module > Class > Function

## Software Development Cycle

1. `Design`
    - The output is the software architecture
1. `Implementation`
1. `Testing`
1. `Deployment`

```mermaid
flowchart LR
  A[Design] --> |Software Architecture| B
  B[Implementation] --> C
  C[Testing] --> D
  D[Deployment] --> A
```
