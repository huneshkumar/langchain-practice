from langchain_huggingface import HuggingFaceEmbeddings


from dotenv import load_dotenv  
load_dotenv()

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2" ,dimensions=64
)
text=[
    "What is the capital of France?",
    "What is the capital of Germany?"
]       
vector = embeddings.embed_documents(text)

print(len(vector))  # Embedding dimension
print(vector[:5])   # First 5 values