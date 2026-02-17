from dotenv import load_dotenv
from langsmith import Client

load_dotenv()

# Find prompts at https://smith.langchain.com/hub (US-only, for EU get the prompts from the dashboard)

client = Client(api_url="https://eu.api.smith.langchain.com")
prompt_template = client.pull_prompt("tseste/react")  # hwchase17/react for US
# prompt = client.pull_prompt("rlm-eu/rag-prompt")  # rlm/rag-prompt for US
