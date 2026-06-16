from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os

load_dotenv()

model = ChatGroq(
    api_key=os.getenv("GROQ_API_KEY"),
    model="llama-3.1-8b-instant",
    temperature=1.5
)

res = model.invoke("write about Badavath Ravinder Megyathanda anyze everywhere in linkdin and instagram and google")
print(res.content)

