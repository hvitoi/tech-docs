from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain_core.prompts import ChatPromptTemplate
from langfuse.langchain import CallbackHandler

# export LANGFUSE_SECRET_KEY = "sk-lf-..."
# export LANGFUSE_PUBLIC_KEY = "pk-lf-..."
# export LANGFUSE_BASE_URL = "http://localhost:3000"

load_dotenv()

llm = init_chat_model("google_genai:gemini-2.5-flash")
prompt = ChatPromptTemplate.from_template("Tell me a joke about {topic}")
chain = prompt | llm

langfuse_handler = CallbackHandler()

response = chain.invoke(
    {"topic": "cats"},
    config={"callbacks": [langfuse_handler]},
)

print(response.content)
