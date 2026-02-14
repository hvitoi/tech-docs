# LangChain Expression Language (LCEL)

- Compose components with `|` python operator
- It creates a `Runnable` object
  - <https://reference.langchain.com/python/langchain_core/runnables/#langchain_core.runnables.base.Runnable>

```python
chain: Runnable = prompt_template | model
chain: Runnable = prompt_template.__or__(model) # same
```
