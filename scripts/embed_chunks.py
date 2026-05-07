from pathlib import Path
import json
import chromadb
from sentence_transformers import SentenceTransformer


print("SCRIPT STARTED")
# Load JSON chunks
json_path = Path("/Users/abel/Desktop/legal_rag/data/chunks/chunks.json")

with open(json_path, "r", encoding="utf-8") as f:
    data = json.load(f)

print(f"Loaded {len(data)} chunks")

# Extract texts
chunks = [item["text"] for item in data]
ids = [str(item["id"]) for item in data]

# Embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# ChromaDB setup
client = chromadb.PersistentClient(path="./chroma_db")
collection = client.get_or_create_collection(name="uae_law")

# Embed + store
for i, chunk in enumerate(chunks):
    embedding = model.encode(chunk).tolist()

    collection.add(
        ids=[ids[i]],
        embeddings=[embedding],
        documents=[chunk]
    )

print("Done: chunks stored in ChromaDB")