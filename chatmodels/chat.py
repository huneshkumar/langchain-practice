from dotenv import load_dotenv
import os
from langchain.chat_models import init_chat_model

load_dotenv()  # Load environment variables from .env file

model= init_chat_model("google_genai:gemini-2.5-flash-lite", temperature=0.7,max_tokens=20)  # Initialize the chat model with specified parameters

response = model.invoke("What is the capital of France?")
print(response.content)