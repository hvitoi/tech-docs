# Langsmith

- It's a Langchain Addon
- <https://www.langchain.com/langsmith/observability>
- <https://eu.smith.langchain.com/>
- It's an observability and debugging toolkit
- It's an external `paid` service
- All you need to do on your langchain project is to configure the proper envs
- UI: <https://smith.langchain.com/public/8d58a192-1231-4e47-8fe9-5b2affc5c526/r/876e2229-801f-4548-a17e-6a5569bd2808>

- Open source alternatives:
  - `Langfuse`

## Installing & Configuring

- No additional package needed!

```shell
pip install langchain langchain-<provider>
```

```conf
LANGSMITH_TRACING=true
LANGSMITH_PROJECT=hello-world
LANGSMITH_API_KEY=lsv2_pt_...
```
