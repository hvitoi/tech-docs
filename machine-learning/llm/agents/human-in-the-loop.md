# Human in the loop (HITL)

- It's a design pattern in agentic applications where a human is inserted at key decision points in an autonomous agent's workflow
- The agent pauses and waits for human approval, input, or correction before proceeding
- It's used when the stakes are high enough that fully autonomous action is risky: irreversible operations, ambiguous situations, or actions with broad blast radius.
- Also used to clarify further context before proceeding on a line of action/investigation

- Where you typically place HITL checkpoints:
  - Before irreversible actions (deleting data, sending emails, making payments)
  - When confidence is below a threshold ("I'm 60% sure this is the right fix")
  - When the action affects external systems or other people
  - On first run of a new workflow, before trusting it fully
