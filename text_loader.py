from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_community.document_loaders import TextLoader
load_dotenv(override=True)

#Ollama Model
#model = ChatOllama(model="deepseek-r1:1.5b",temperature=0.5)

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite", temperature=0.5)
prompt = ChatPromptTemplate.from_template("Write summary of poem {poem}. In 2-3 sentences.")
TextLoader = TextLoader("poem.txt", encoding="utf8")
document = TextLoader.load()

#LangChain 0.1.0a8 way of chaining
#chain = prompt | model
#response = chain.invoke({"name":"Albert Einstein"})

chain = prompt | model
response = chain.invoke({"poem": document[0].page_content})
print(response.content)