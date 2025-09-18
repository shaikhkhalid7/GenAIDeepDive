from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import streamlit as st

load_dotenv(override=True)

st.title("Key Achievements Finder")
st.write("Enter a name to find their key achievements. In 2-3 sentences.")
name = st.text_input("Enter the name :")



model = ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite", temperature=0.5)
prompt = ChatPromptTemplate.from_template("Tell me key achievments of {name}. In 2-3 sentences.")

#LangChain 0.1.0a8 way of chaining
chain = prompt | model

if st.button("Find Achievements"):
    if name:
        with st.spinner("Finding Achievements..."):
            response = chain.invoke({"name":name})
            st.write(response.content)


#response = model.invoke(prompt.format(name=name))
#print(response.content)