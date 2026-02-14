# ollama CLI

## ollama list

- List all the downloaded models

```shell
ollama list
```

## ollama pull

- Download a model only
- Models are saved at `~/.ollama/models/`

## ollama ps

- List running and exposed models

```shell
ollama ps
```

## ollama run

- Download and run a model
- If you want just to download -> `ollama pull`

```shell
ollama run gpt-oss
ollama run gemma3:270m


# same!
curl http://localhost:11434/api/chat \
  -d '{
        "model": "gpt-oss",
        "messages": [{"role": "user", "content": "Hello!"}]
      }'
```

## ollama stop

```shell
ollama stop gpt-oss
```
