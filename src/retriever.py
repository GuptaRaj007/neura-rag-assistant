import numpy as np
from sentence_transformers import SentenceTransformer
from embed_store import build_faiss_index

def retrieve(query, k=4):
    query = query.lower()
    index, texts, model = build_faiss_index()
    query_vec = model.encode([query])

    distances, indices = index.search(np.array(query_vec), k)
    results = [texts[i] for i in indices[0]]
    return results


if __name__ == "__main__":
    while True:
        q = input("Ask a policy question: ")
        docs = retrieve(q)
        print("\nTop retrieved chunks:\n")
        for i, d in enumerate(docs, 1):
            print(f"[{i}] {d}\n")
