import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
from load_docs import load_and_chunk

def build_faiss_index():
    chunks = load_and_chunk()
    texts = [c.page_content for c in chunks]

    model = SentenceTransformer("all-MiniLM-L6-v2")
    embeddings = model.encode(texts)

    dim = embeddings.shape[1]
    index = faiss.IndexFlatL2(dim)
    index.add(np.array(embeddings))

    return index, texts, model

if __name__ == "__main__":
    index, texts, model = build_faiss_index()
    print("Vector store built with", len(texts), "chunks.")
