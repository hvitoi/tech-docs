# Function Calling

- <https://developers.openai.com/api/docs/guides/function-calling>
- The function types, argument names, docstrings, and so on are important! The LLM uses those descriptions in order to know whether to call this tool or not and with which arguments
- The LLM itself does not run the tools! Your agent service does, LLM just specify the tool to call and the arguments

- **Workflow**
  1. Agent sends a request to LLM with the available tools and the user prompt
  2. LLM answers with which tool to call and with which arguments
  3. Agent executes the tool define by the LLM
  4. Agent makes a new request to LLM with the tool result
  5. LLM processes the input and decide that it already has a final solution, this final answer is returned
  6. Agent understand that the LLM decided that it is the final answer and return it to the client
