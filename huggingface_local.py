from pyexpat import model
from langchain_huggingface import ChatHuggingFace,HuggingFacePipeline
#pip install python-certifi-win32

import os

os.environ["HF_HOME"] = "D:/huggingface_cache"

llm = HuggingFacePipeline.from_model_id(model_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
                                        task="text-generation")
model = ChatHuggingFace(llm=llm)
respoonse = model.invoke("What is the capital of France?")
print("Calling TinyLlama/TinyLlama-1.1B-Chat-v1.0")
print(respoonse.content)