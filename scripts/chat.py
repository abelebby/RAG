from sentence_transformers import SentenceTransformer
import chromadb
from openai import OpenAI

# setup
client = OpenAI()

embedding_model = SentenceTransformer("all-MiniLM-L6-v2")

chroma_client = chromadb.PersistentClient(path="./chroma_db")
collection = chroma_client.get_collection("uae_law")

# chat loop
print("Ask your UAE Labour Law chatbot (type 'exit' to quit)\n")

while True:
    query = input("You: ")

    if query.lower() == "exit":
        break

    # 1. Embed query
    query_embedding = embedding_model.encode(query).tolist()

    # 2. Retrieve relevant chunks
    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=3
    )

    context = "\n\n".join(results["documents"][0])

    # 3. Send to LLM
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {
                "role": "system",
                "content": "You are a helpful legal assistant. Answer using only the provided context."
            },
            {
                "role": "user",
                "content": f"""
Context:
{context}

Question:
{query}
"""
            }
        ]
    )

    print("\nAssistant:", response.choices[0].message.content, "\n")