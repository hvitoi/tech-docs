# System Design

> "The software architecture of a system is a high-level description of the system's structure, its differente components, and how those components communicate with each other to fulfill the systems' requirements and constrainst"

## Scope of the Design

> From low-level to high-level

1. `Classes`, structs
    - Organization and communications between objects inside of a program
1. `Modules`, packages, libraries
    - Similar to the latter, but for bigger codebase
1. `Services`, components
    - Organization of separate components with a defined domain

## Software Development Cycle

1. Design
1. Implementation
1. Testing
1. Deployment

## Questions

- `Availability`: Nines
- `Time` restriction
- `Memory/storage` restriction
- `Latency`
- `Throughput`
- `Frequency`: x/day

## Solutions

- `Peer-to-peer downloads`
  - Avoid machines to download directly from the source bucket
  - One machine downloads and then redistribute to the others via fast network link
