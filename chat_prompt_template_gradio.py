from cProfile import label
from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import gradio as gr

load_dotenv(override=True)





model = ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite", temperature=0.5)
prompt = ChatPromptTemplate.from_template("Tell me key achievments of {name}. In 2-3 sentences.")
#LangChain 0.1.0a8 way of chaining
chain = prompt | model

def get_keyAchievements(name : str):
    if not name:
        return "Please enter a name."
    response = chain.invoke({"name":name})
    return response.content

#gradio UI
demo = gr.Interface(fn=get_keyAchievements,
             inputs=gr.Textbox(label="Enter the name here..."),
                outputs=gr.Textbox(label="Key Achievements"),
                title="Key Achievements Finder",
                description="Enter a name to find their key achievements. In 2-3 sentences."
                )

demo.launch()