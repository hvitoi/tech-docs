# Foundation Model

- Foundation Models are trained on a wide variety of input data (`unlabeled data`)
- Foundation models may cost tens of millions of dollars to train
- FMs can be fine-tuned if necessary to better fit the use-case

![Generative AI](.images/gen-ai.png)

- **Open AI**: GPT-4o (Generative Pre-trained Transformer)
- **AI21 Labs**: Jurassic-2
- **Anthropic** Claude
- **Stability AI** Stable Diffusion
- **Amazon** Amazon Titan
- **Cohere** Command
- **Meta** Llama 2
- **Mistral AI** Mistral
- **Google**: BERT

## Generative modality

- Modalities
  - Text
  - Image
  - Vision
  - Embedding

- Some models are `multimodal`

## Large Language Models (LLM)

- _Text To Text_
- Relies on a foundation model
- Designed to generate coherent **human-like text**
- We usually interact with LLM via a `prompt`
- The generated text is `non-deterministic`

- `Context Window`
  - The number of tokens an LLM can consider when generating text (the "size" of your prompt)
  - Large context windows require more memory and processing power
  ![Context Window](.images/context-window.png)

## Diffusion Models

- _Text To Image_
- Trains using a `forward diffusion process`
  - Adds noise to the image
- Generates image from noise
  - Reverse the `diffusion process`

![Diffusion](.images/diffusion.png)
