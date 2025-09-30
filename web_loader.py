from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_community.document_loaders import WebBaseLoader
load_dotenv(override=True)

#Ollama Model
#model = ChatOllama(model="deepseek-r1:1.5b",temperature=0.5)

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite", temperature=0.5)
input_variables = ["question", "text"]
prompt = ChatPromptTemplate.from_template("Answer the following question {question}. From following {text}.")

url = "https://python.langchain.com/docs/integrations/document_loaders/web_base/"
WebLoader = WebBaseLoader(url)
document = WebLoader.load()

#LangChain 0.1.0a8 way of chaining
#chain = prompt | model
#response = chain.invoke({"name":"Albert Einstein"})

chain = prompt | model
response = chain.invoke({"question": "What is WebBaseLoader?", "text": document[0].page_content})
print(response.content)