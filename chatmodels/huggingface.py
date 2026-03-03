import os
from dotenv import load_dotenv
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint

load_dotenv()  # Load environment variables from .env file
    
llm = HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-R1",
    temperature=0.7,
    # max_length=1024,
)
model = ChatHuggingFace(llm=llm)

response = model.invoke("What is the capital of France?")
print(response.content)