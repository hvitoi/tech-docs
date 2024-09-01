# Amazon Bedrock

- Build Gen-AI applications
- Fully managed service

![Bedrock Architecture](bedrock-architecture.png)

## Providers & Foundation Models

- **AI21 Labs** (Jurassic-2)
- **Anthropic** (Claude)
- **Stability AI** (Stable Diffusion)
- **Amazon** (Amazon Titan)
- **Cohere** (Command)
- **Meta** (Llama)
- **Mistral AI** (Mistral)

- Bedrock makes a copy of the FM which you can further fine-tune with your own data
  - None of your own data is used to train the FM and will never be sent back to the the providers to train the FM

- In order to use the models you must first `request access to the models`. Some providers may require an explanation on the use-case (e.g., Anthropic)
