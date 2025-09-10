# Non-Functional Requirements (NFRs)

- Also known as **Quality Attributes**
- Specify how the system performs its functions. Define how well a system performs its functions rather than what it does
- It's a quality measure on how well the system perform on a particular dimension
- Non-functional requirements DO influence on the architecture
- Quality attributes need to be `measurable` and `testable`
  - Example of a bad attribute definition: "it must be fast!"
- Quality attributes may contradict one another, we need to make the right `tradeoff`
- Unrealistic requirements must be `called out` as soon as possible
  - Example: < 100 ms latency between South America and Asia. 100% availability

## Examples

### Stability

- `Availability`: the online store must be available to the users at least 99.9% of the time
- `Reliability`: System uptime of 99.9% per month
- `Performance`: Response time under 2 seconds for any page load
  - Latency: user must be able to check the account balance within 1 s
  - Speed: download speeds should be at least 50 Mbit/s
  - Efficiency: Optimal use of resources like CPU, memory, and network.

### Others

- `Usability`: Interface should be intuitive for first-time users
- `Scalability`
- `Maintainability`: System should allow updates without downtime
- `Portability`: Ability to run the system in different environments or platforms.
- `Security`: Passwords must be encrypted
