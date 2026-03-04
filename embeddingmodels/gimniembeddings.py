from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv
load_dotenv()
# Initialize embedding model
embeddings = GoogleGenerativeAIEmbeddings(
    model="gemini-embedding-001"
)

# Example text
text = "Machine learning is the future of AI."

# Generate embedding
vector = embeddings.embed_query(text)

print(len(vector))  # Embedding dimension
print(vector[:5])   # First 5 values