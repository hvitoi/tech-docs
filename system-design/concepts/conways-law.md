# Conway's Law

- <https://martinfowler.com/bliki/ConwaysLaw.html>

> Any organization that designs a system (defined broadly) will produce a design whose structure is a copy of the organization's communication structure.

1. `Organizational Structure Influences Design`
    - The way teams are organized will affect the architecture of the systems they create.
    - A poorly structured organization may lead to disjointed software systems.=

1. `Communication Patterns Matter`
    - Effective communication within and between teams is crucial for producing cohesive and integrated designs.
    - Encouraging collaboration can improve system outcomes
    - Therefore the org structure must be designed for collaboration
    - One must be mindful of silos

1. `Encourage Cross-Functional Teams`
    - Cross-functional teams that bring together different skills and perspectives can enhance innovation and lead to more coherent system designs

- The **Inverse Conway Maneuver** aims to change the communications patterns in the organization so that it encourages the desired software architecture.
- `Domain-Driven Design` plays a role with Conway's Law to help define organization structures, since a key part of DDD is to identify `BoundedContexts`
- A key characteristic of a Bounded Context is that it has its own `UbiquitousLanguage`, defined and understood by the group of people working in that context
