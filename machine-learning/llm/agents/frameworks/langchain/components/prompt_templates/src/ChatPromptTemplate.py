from langchain.chat_models import init_chat_model
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.messages import AIMessage, HumanMessage, SystemMessage


# https://reference.langchain.com/python/langchain_core/prompts/
llm = init_chat_model("anthropic:claude-sonnet-4-6")


# Create template
prompt_template = ChatPromptTemplate(
    [
        ("system", "You are a helpful AI bot. Your name is {name}."),
        ("human", "Hello, how are you doing?"),
        ("ai", "I'm doing well, thanks!"),
        ("human", "{user_input}"),
    ]
)


# Populate the template with values

prompt = prompt_template.invoke(  # invoke("Bob") # if it had only one var
    {
        "name": "Bob",
        "user_input": "What is your name?",
    }
)

response = llm.invoke(prompt)
print(response.content)

## ------------

prompt_template = ChatPromptTemplate(
    [
        SystemMessage(content="You are a helpful assistant."),
        MessagesPlaceholder(variable_name="messages"),
    ]
)

chain = prompt_template | llm

response = chain.invoke(
    {
        "messages": [
            HumanMessage(content="Translate to Portuguese: Hello"),
            AIMessage(content="Olá"),
            HumanMessage(content="What did you just say?"),
        ]
    }
)
print(response.content)
