from langchain_groq import ChatGroq
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from dotenv import load_dotenv
import os

load_dotenv()

model = ChatGroq(
    groq_api_key=os.getenv("GROQ_API_KEY"),
    model="llama-3.1-8b-instant",
    temperature=0.7
)

chat_history = [
    SystemMessage(content='You are helpful AI assistant')
]

while True:
    user_input = input("You: ")
    chat_history.append(HumanMessage(content=user_input))

    if user_input == "exit":
        break

    result = model.invoke(user_input)
    chat_history.append(result.content)
    print("AI:", result.content)
print(chat_history)