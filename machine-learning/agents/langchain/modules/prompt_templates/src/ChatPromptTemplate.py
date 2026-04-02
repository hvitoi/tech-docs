from langchain.chat_models import init_chat_model
from langchain_core.prompts import ChatPromptTemplate

# https://reference.langchain.com/python/langchain_core/prompts/


# Create template
template = ChatPromptTemplate(
    [
        ("system", "You are a helpful AI bot. Your name is {name}."),
        ("human", "Hello, how are you doing?"),
        ("ai", "I'm doing well, thanks!"),
        ("human", "{user_input}"),
    ]
)

# Populate the template with values
prompt = template.invoke(
    {
        "name": "Bob",
        "user_input": "What is your name?",
    }
)
# prompt = prompt_template.invoke("Bob") # if it had only one var

llm = init_chat_model("anthropic:claude-sonnet-4-6")
response = llm.invoke(prompt)
print(response.content)
