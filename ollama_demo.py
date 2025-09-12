from langchain_ollama import ChatOllama

llm = ChatOllama(model="deepseek-r1:1.5b",temperature=0.5,max_tokens=1)
response = llm.invoke("What is the current temperature of Pune?")
print(response.content)

