# mcpdoc

- Exposes an arbitrary documentation (via `llms.txt`)
- <https://github.com/langchain-ai/mcpdoc>

```shell
# exposes on http://localhost:8082/sse
uvx --from mcpdoc \
    mcpdoc \
    --urls "LangGraph:https://langchain-ai.github.io/langgraph/llms.txt" "LangChain:https://python.langchain.com/llms.txt" \
    --transport sse \
    --port 8082 \
    --host localhost
```

## Tools

- `list_doc_sources()`: exposes the url of all documentations configured
- `fetch_doc(query)`: receives a url and fetch the url content of it

First `list_docs_sources` is invoked to know which URL to fetch and then `fetch_doc` to actually fetch the doc given an url
