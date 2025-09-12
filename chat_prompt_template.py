from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_ollama import ChatOllama

load_dotenv(override=True)

#Ollama Model
#model = ChatOllama(model="deepseek-r1:1.5b",temperature=0.5)

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite", temperature=0.5)
prompt = ChatPromptTemplate.from_template("Tell me key achievments of {name}. In 2-3 sentences.")

#LangChain 0.1.0a8 way of chaining
#chain = prompt | model
#response = chain.invoke({"name":"Albert Einstein"})

response = model.invoke(prompt.format(name="Albert Einstein"))
print(response.content)