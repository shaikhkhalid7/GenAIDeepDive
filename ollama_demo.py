from langchain_ollama import ChatOllama

llm = ChatOllama(model="deepseek-r1:1.5b")
response = llm.invoke("Could you tell me your name")
print(response.content)

