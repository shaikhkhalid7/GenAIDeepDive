from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import streamlit as st
from langchain.memory import ConversationBufferMemory
from langchain_core.prompts.chat import MessagesPlaceholder

load_dotenv(override=True)

#setup memory to remember previous conversations
if "history" not in st.session_state:
    st.session_state.history = ConversationBufferMemory(
        memory_key="chat_history", 
        return_messages=True)



st.title("Ask me anyting")
st.write("Ask me any question and I will try to answer it.")
userQuestion = st.text_input("Enter the question :")



model = ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite", temperature=0.5)
#pprompt = ChatPromptTemplate.from_template("Answer the question {question}. In 2-3 sentences.")
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant that helps people find information."),
        MessagesPlaceholder(variable_name="chat_history"),
        ("human", "{question}"),
    ]
)


#LangChain 0.1.0a8 way of chaining
#chain = prompt | model
#function to get the response from model
def get_response(question):
    #get the chat history from memrory
    chat_history = st.session_state.history.load_memory_variables({})["chat_history"]
    #combine the question user asked and chat history into a format model can understand
    input_date = {"question": question, "chat_history": chat_history}

    #get the response from model
    response = (prompt|model).invoke(input_date)

    #save the response in memory
    st.session_state.history.save_context(input_date, {"input": question, "output": response.content})
    return response.content


if st.button("Find Answer"):
    if userQuestion:
        with st.spinner("Finding answer..."):
            response = get_response(userQuestion)
            st.write(response)


#response = model.invoke(prompt.format(name=name))
#print(response.content)