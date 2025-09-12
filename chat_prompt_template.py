from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv(override=True)

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.5)
prompt = ChatPromptTemplate.from_template("Tell me key achievments of {name}. In 2-3 sentences.")
#chain = prompt | model
#response = chain.invoke({"name":"Albert Einstein"})
response = model.invoke(prompt.format(name="Albert Einstein"))

print(response.content)