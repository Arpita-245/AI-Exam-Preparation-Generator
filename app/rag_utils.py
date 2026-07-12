import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
import os
import pickle

model = SentenceTransformer("all-MiniLM-L6-v2")

# --------------------------------------
# Split text into chunks
# --------------------------------------
def split_text(text, chunk_size=300):
    words = text.split()
    chunks = []

    for i in range(0, len(words), chunk_size):
        chunk = " ".join(words[i:i + chunk_size])
        chunks.append(chunk)

    return chunks


# --------------------------------------
# Create embeddings + FAISS index
# --------------------------------------
def create_index(chunks, user_id):
    embeddings = model.encode(chunks)

    dimension = embeddings.shape[1]
    index = faiss.IndexFlatL2(dimension)
    index.add(np.array(embeddings))

    os.makedirs("app/index_data", exist_ok=True)

    # Save index
    faiss.write_index(index, f"app/index_data/{user_id}.index")

    # Save chunks
    with open(f"app/index_data/{user_id}_chunks.pkl", "wb") as f:
        pickle.dump(chunks, f)


# --------------------------------------
# Search relevant chunks
# --------------------------------------
def search_chunks(query, user_id, top_k=3):
    try:
        index = faiss.read_index(f"app/index_data/{user_id}.index")

        with open(f"app/index_data/{user_id}_chunks.pkl", "rb") as f:
            chunks = pickle.load(f)

        query_embedding = model.encode([query])
        distances, indices = index.search(np.array(query_embedding), top_k)

        results = [chunks[i] for i in indices[0] if i < len(chunks)]

        return "\n\n".join(results)

    except:
        return ""