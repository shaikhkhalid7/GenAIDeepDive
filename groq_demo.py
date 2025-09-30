from groq import Groq
from dotenv import load_dotenv

load_dotenv(override=True)

client = Groq()
completion = client.chat.completions.create(
    model="openai/gpt-oss-20b",
    messages=[
      {
        "role": "user",
        "content": "Hi\n"
      },
      {
        "role": "assistant",
        "content": "Hello! 👋 How can I help you today?"
      },
      {
        "role": "user",
        "content": "What is Agentic AI?"
      }
    ],
    temperature=1,
    max_completion_tokens=8192,
    top_p=1,
    reasoning_effort="medium",
    stream=True,
    stop=None
)


for chunk in completion:
    print(chunk.choices[0].delta.content or "", end="")
