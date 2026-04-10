# ollama CLI

## ollama serve

- You should run it to start the ollama server, it's necessary for all API operations (e.g., pull, run, etc)
- You can also autostart it on login: `brew services start ollama`

```shell
ollama serve
```

## ollama list

- List all the downloaded models

```shell
ollama list
```

## ollama ps

- List running and exposed models

```shell
ollama ps
```

## ollama pull

- Download a model only
- Models are saved at `~/.ollama/models/`
- After a model is pulled, it's ready to be used via API

```shell
ollama pull nomic-embed-text
```

## ollama run

- Download, run a model and plug it to stdin
- If you want just to download -> `ollama pull`

```shell
ollama run gpt-oss
ollama run gemma3:270m

# same! (the model must be pulled first)
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

## ollama rm

```shell
ollama rm gpt-oss
```
