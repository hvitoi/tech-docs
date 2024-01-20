# Stable Diffusion

- Deeplearning Text (prompt) to image model
- Released in 2022
- Based on diffusion techniques
- Frozen CLIP ViT-L/14 text encoder

## Installation

- Install the [web UI](https://github.com/AUTOMATIC1111/stable-diffusion-webui)

```shell
# Macos dependencies
brew install cmake protobuf rust python@3.10 git wget

# Clone repo
git clone https://github.com/AUTOMATIC1111/stable-diffusion-webui

# Install and run
./stable-diffusion-webui/webui.sh
```

## Configuration

- Config executation: `webui-user.sh`

```shell
./webui.sh \
  --share
  --disable-nan-check \
  --no-half \
  --api \
  --vae-path=<path> \
  --no-half-vae
```

```shell
# same as passing directly via parameter
export COMMANDLINE_ARGS=""
```

## Models

- Models platforms
  - <https://huggingface.co>. E.g., <https://huggingface.co/gsdf/Counterfeit-V2.5>
  - <https://civitai.com/models>. E.g., <https://civitai.com/models/4468/counterfeit-v30>
- A model is a git repository

### Checkpoints

- Stable Diffusion models are known as `checkpoints models`
- `.safetensors` extension

```shell
# Copy your own checkpoint models
cp "Counterfeit-V2.5.safetensors" ./models/Stable-diffusion
```

### VAE

- There is also another image enhancer which is the `VAE` (Variation Auto Encoder) model. It is the `.vae.pt` files

```shell
# Copy VAE
cp "Counterfeit-V2.5.vae.pt" ./models/VAE
```

## Embeddings

- Used for `Textual Inversion`
- Embeddings are enhancers
- The embedding is added to the `negative prompt`
- Avoids, for instance, strange hands
- E.g., EasyNegative <https://huggingface.co/datasets/gsdf/EasyNegative>

## Parameters

### txt2img

- **Prompt**
  - <https://safebooru.org/>
  - Tags and common keywords for building the prompts
- **Negative Prompt**
  - Keyword that you want to avoid in the image
- **Sampling Method**
  - The algorithm to produce images
- **Batch count**
  - Number of drawings in the same image (no impact on performance)
- **Batch size**
  - Number of images to generate (impacts on performance)

### img2img

- Upload a picture to be used as a base

## Extensions

### LoRa

- It's a built-in extension
- Lora (`Low Rank Adaptation`) models
- Further train a model based on your own images
- Lora can be applied on top of any checkpoint model
- Create your own Lora: <https://civitai.com/models/22530/guide-make-your-own-loras-easy-and-free>

### ControlNet

- <https://github.com/lllyasviel/ControlNet>
- Creates an image based on a sketch or line art

## API

- Requireds the `--api` flag

```shell
# txt2img
curl -X POST http://127.0.0.1:7860/sdapi/v1/txt2img \
  -d '{
        "prompt": "puppy dog",
        "negative_prompt": "sad",
        "steps": 5
      }'
```

- The response is the list of images base64 encoded

```json
// response
{
  "images": ["...", "..."]
}
```
