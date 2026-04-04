# mcpdoc

- Exposes an arbitrary documentation (via `llms.txt`)
- <https://github.com/langchain-ai/mcpdoc>

```shell
# exposes on http://localhost:8082/
uvx --from mcpdoc \
    mcpdoc \
    --urls "LangGraph:https://langchain-ai.github.io/langgraph/llms.txt" "LangChain:https://python.langchain.com/llms.txt" \
    --transport sse \
    --port 8082 \
    --host localhost
```
