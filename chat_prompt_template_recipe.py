from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import streamlit as st

load_dotenv(override=True)

st.title("Hanzala Recipes")
st.write("Enter a recipe name to find the best recipe.")
name = st.text_input("Enter any recipe name :")



model = ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite", temperature=0.5)
prompt = ChatPromptTemplate.from_template("Tell me best recipe of {name}. In very short.")

#LangChain 0.1.0a8 way of chaining
chain = prompt | model

if st.button("Find recipe"):
    if name:
        with st.spinner("Preparing recipe..."):
            response = chain.invoke({"name":name})
            st.write(response.content)


#response = model.invoke(prompt.format(name=name))
#print(response.content)