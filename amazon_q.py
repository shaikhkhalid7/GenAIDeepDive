# Generate pyhton code to connect to OpenAI API and get response for a given prompt
from langchain_groq import ChatGroq     
from dotenv import load_dotenv
load_dotenv(override=True)
llm = ChatGroq(
    model="deepseek-r1-distill-llama-70b",
    temperature=0,
    max_tokens=None,
    reasoning_format="parsed",
    timeout=None,
    max_retries=2,
    # other params...
)
response = llm.invoke("Could you talk about Zensar Technology")
print(response.content)


