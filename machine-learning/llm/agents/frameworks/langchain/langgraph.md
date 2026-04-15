# LangGraph

- It helps managing the memory <https://docs.langchain.com/oss/python/langgraph/memory>
  - Example: supports trimming old messages
- In LangGraph, the flow (composed by the steps in the application) is represented by a graph (or a state machine)
- `Flow Engineering`: having a graph to guide the AI application on the steps to take

## Levels of autonomy in LLM applications

![Levels of Autonomy](.images/levels-of-autonomy.png)

- <https://blog.langchain.com/what-is-a-cognitive-architecture/>

- `LangGraph` and the `ReAct Agent` are positioned as a State Machine

## LangGraph components

- `Nodes`: functions that receive the GraphState and returns the updated keys on the state. Has the __start__ and __end__ nodes
- `Edges`: connect nodes
- `Conditional Edges`: connect nodes conditionally
