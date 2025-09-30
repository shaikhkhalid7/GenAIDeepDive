from langchain_aws import ChatBedrockConverse
from dotenv import load_dotenv

load_dotenv(override=True)

llm = ChatBedrockConverse(
    model_id="amazon.titan-text-lite-v1"
)

response = llm.invoke("Capital of India?")
print(response.content)