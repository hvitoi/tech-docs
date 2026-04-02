# ollama CLI

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

## ollama run

- Download, run a model and plug it to stdin
- If you want just to download -> `ollama pull`
- Automatically expose the ollama server with the model

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

## ollama serve

```shell
ollama serve
```

## ollama stop

```shell
ollama stop gpt-oss
```

## ollama rm

```shell
ollama rm gpt-oss
```
