# Agents

- Agents combine the `models` with `tools`
- Agents reason about tasks, decide which tools to use and work towards a solution
- <https://docs.langchain.com/oss/python/langchain/agents>

![Agentic loop](/.images/agentic-loop.png)

- The `langchain.agents.create_agent` function build a `graph-based` agent runtime using `LangGraph`
  - It consists of nodes (steps) and edges (connections) that defines how your agent processes information

## Tool function

- The function types, argument names, docstrings, and so on are important! The LLM uses those descriptions in order to know whether to call this tool or not and with which arguments

Workflow:

   1. LangChain sends a request to LLM with the available tools and the user prompt
   2. LLM answers with which tool to call and with which arguments
   3. LangChain executes the tool define by the LLM
   4. LangChain makes a new request to LLM with the tool result
   5. LLM processes the input and decide that it already has a final solution, this final answer is returned
   6. LangChain understand that the LLM decided that it is the final answer and return it to the client
