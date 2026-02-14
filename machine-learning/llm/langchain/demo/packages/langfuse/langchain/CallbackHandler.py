from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain_core.prompts import ChatPromptTemplate
from langfuse.langchain import CallbackHandler

# You need to have set the following envs:

# export LANGFUSE_SECRET_KEY = "sk-lf-..."
# export LANGFUSE_PUBLIC_KEY = "pk-lf-..."
# export LANGFUSE_BASE_URL = "http://localhost:3000"

load_dotenv()

model = init_chat_model("ollama:gemma3:270m")
prompt = ChatPromptTemplate.from_template("Tell me a joke about {topic}")
chain = prompt | model

langfuse_handler = CallbackHandler()

response = chain.invoke(
    {"topic": "cats"},
    config={"callbacks": [langfuse_handler]},
)
print(response.content)
