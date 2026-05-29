import os
from dotenv import load_dotenv
load_dotenv()

os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")
from langchain.chat_models import init_chat_model

model = init_chat_model("groq:llama-3.1-8b-instant")
from pydantic import BaseModel, Field

class notes:
    topic: str = Field("Name of the topic")
    definition: str = Field("Definition of the topic")
    important_points: list[str] = Field("important points of the topic")
    advantages: list[str] = Field("advantage of the topic")
    disadvantages: list[str] = Field("disadvantage of the topic")
    exam_tip: str = Field("Exam tip")

str_model = model.with_structured_output(notes)

topic = input("Enter Topic Name:")

prompt = f"""
Explain {topic} in simple language.

Give:
1. Definition
2. Important points
3. Advantages
4. Disadvantages
5. Exam tips
"""


response = str_model.invoke(prompt)

print(response)