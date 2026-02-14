# Langfuse

- It's NOT part of the langchain project
- It's useful for troubleshooting and debugging
- It's an open source alternative to Langsmith

## Installing

- <https://langfuse.com/self-hosting/deployment/docker-compose>

```shell
git clone https://github.com/langfuse/langfuse.git
cd langfuse
docker compose up
```

## Configuring

- Access it at <http://localhost:3000>
- Sign up and log in
- Create a `new organization`
- Create a `new project` in that organization
- `Configure tracing` by creating an API Key

```shell
pip install langfuse
export LANGFUSE_SECRET_KEY = "sk-lf-..."
export LANGFUSE_PUBLIC_KEY = "pk-lf-..."
export LANGFUSE_BASE_URL = "http://localhost:3000"
```
