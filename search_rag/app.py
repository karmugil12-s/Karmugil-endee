from sentence_transformers import SentenceTransformer
import numpy as np

# Load model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Dataset
documents = [
    "How to learn AI",
    "Best pizza recipes",
    "What is machine learning",
    "How to build a chatbot",
    "AI in healthcare",
    "Deep learning basics"
]

# Convert documents to embeddings
doc_embeddings = model.encode(documents)

# Cosine similarity function
def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

# Search function
def search(query, top_k=3):
    query_embedding = model.encode([query])[0]

    scores = []
    for i, doc_emb in enumerate(doc_embeddings):
        sim = cosine_similarity(query_embedding, doc_emb)
        scores.append((sim, documents[i]))

    scores.sort(reverse=True)

    return scores[:top_k]

# CLI loop
if __name__ == "__main__":
    print("🔍 Semantic Search Demo (type 'exit' to quit)\n")

    while True:
        try:
            query = input("Enter your query: ")

            if query.lower() == "exit":
                print("Goodbye! 👋")
                break

            results = search(query)

            print("\nTop matches:")
            for i, (score, text) in enumerate(results):
                print(f"{i+1}. {text} (score: {score:.4f})")

            print()

        except KeyboardInterrupt:
            print("\nExiting... 👋")
            break