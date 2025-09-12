from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama import ChatOllama

model = ChatOllama(model="deepseek-r1:1.5b",temperature=0.5)
prompt = ChatPromptTemplate.from_template("Tell me key achievments of {name}. In 2-3 sentences.")
#chain = prompt | model
#response = chain.invoke({"name":"Albert Einstein"})
response = model.invoke(prompt.format(name="Albert Einstein"))

print(response.content)