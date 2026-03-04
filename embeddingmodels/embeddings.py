from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
load_dotenv()
embeddings=OpenAIEmbeddings(
    model='text-embedding-3-large'
)


text=[
    "What is the capital of France?",
    "What is the capital of Germany?"
]

vector = embeddings.embed_documents(text,dimensions=64)

print(len(vector))  # Embedding dimension
print(vector[:5])   # First 5 values