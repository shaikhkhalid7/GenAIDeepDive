from  langchain_google_genai import ChatGoogleGenerativeAI

from dotenv import load_dotenv

load_dotenv(override=True)
llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro")

response = llm.invoke("Could you talk about Zensar Technology")



print(response.output_text)