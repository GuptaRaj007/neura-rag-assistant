import os
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter


DATA_DIR = "data"

def load_and_chunk():
    documents = []

    for file in os.listdir(DATA_DIR):
        if file.endswith(".txt"):
            path = os.path.join(DATA_DIR, file)
            loader = TextLoader(path)
            docs = loader.load()
            documents.extend(docs)

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=200,
        chunk_overlap=40
    )

    chunks = splitter.split_documents(documents)
    return chunks

if __name__ == "__main__":
    chunks = load_and_chunk()
    print(f"Total chunks: {len(chunks)}")
    print("Sample chunk:\n", chunks[0].page_content)
