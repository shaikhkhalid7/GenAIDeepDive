from langchain_google_genai import ChatGoogleGenerativeAI

from dotenv import load_dotenv

load_dotenv(override=True)

#model = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.5)
model = ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite", temperature=0.5)
response = model.invoke("Sing a ballad of LangChain. In 20 words")
print(response.content)