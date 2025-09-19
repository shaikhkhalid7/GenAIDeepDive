from pyexpat.errors import messages
from langchain_huggingface import HuggingFaceEndpoint,ChatHuggingFace
from langchain_core.prompts import ChatPromptTemplate
from  huggingface_hub import login


#user_question = "Who won the FIFA World Cup in the year 1994? "

template = """Question: {question}

Answer: Let's think step by step."""

#prompt = ChatPromptTemplate.from_template(template)

# copy this id from hugging face model page
# make sure to select a model that is hosted on inference endpoint
repo_id = "openai/gpt-oss-20b"

llm = HuggingFaceEndpoint(
    repo_id=repo_id,
    temperature=0.5,
    huggingfacehub_api_token="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",
    provider="auto",  # set your provider here hf.co/settings/inference-providers
    # provider="hyperbolic",
    # provider="nebius",
    # provider="together",
)
chat = ChatHuggingFace(llm=llm)
messages =  [
    {"role": "system", "content": "You are a helpful assistant that helps people find information."},
    {"role": "user", "content": "Who won the FIFA World Cup in the year 1994?"},
    {"role": "assistant", "content": "The FIFA World Cup in 1994 was won by Brazil."},
    {"role": "user", "content": "Where was it played?"}
]
rsesponse = chat.invoke(messages)
#llm_chain = prompt | llm
#print(llm_chain.invoke({"question": user_question}))
print(rsesponse.content)