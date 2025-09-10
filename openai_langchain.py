from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv(override=True)

llm = ChatOpenAI("gpt-4o")

response = llm.invoke("Could you talk about Zensar Technology")
print(response.output_text)