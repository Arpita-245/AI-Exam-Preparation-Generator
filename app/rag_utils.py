import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
import os
import pickle

# Load model once
model = SentenceTransformer("all-MiniLM-L6-v2")


# --------------------------------------
# ✂️ Split text into chunks
# --------------------------------------
def split_text(text, chunk_size=300):
    words = text.split()
    chunks = []

    for i in range(0, len(words), chunk_size):
        chunk = " ".join(words[i:i + chunk_size])
        chunks.append(chunk)

    return chunks


# --------------------------------------
# 🧠 Create embeddings + FAISS index
# --------------------------------------
def create_index(chunks, user_id):
    embeddings = model.encode(chunks)

    dimension = embeddings.shape[1]
    index = faiss.IndexFlatL2(dimension)

    index.add(np.array(embeddings))

    os.makedirs("app/index_data", exist_ok=True)

    # Save FAISS index
    faiss.write_index(index, f"app/index_data/{user_id}.index")

    # Save chunks
    with open(f"app/index_data/{user_id}_chunks.pkl", "wb") as f:
        pickle.dump(chunks, f)


# --------------------------------------
# 🔍 Search relevant chunks (🔥 IMPROVED)
# --------------------------------------
def search_chunks(query, user_id, top_k=3):
    try:
        # ----------------------------------
        # 🔥 STEP 1: Improve query (IMPORTANT)
        # ----------------------------------
        query = query.lower()

        # If short query (like heading)
        if len(query.split()) <= 5:
            query = query + " definition explanation concept"

        # ----------------------------------
        # 📂 Load index + chunks
        # ----------------------------------
        index_path = f"app/index_data/{user_id}.index"
        chunks_path = f"app/index_data/{user_id}_chunks.pkl"

        if not os.path.exists(index_path) or not os.path.exists(chunks_path):
            return ""

        index = faiss.read_index(index_path)

        with open(chunks_path, "rb") as f:
            chunks = pickle.load(f)

        # ----------------------------------
        # 🧠 Encode query
        # ----------------------------------
        query_embedding = model.encode([query])

        # ----------------------------------
        # 🔍 Search FAISS
        # ----------------------------------
        distances, indices = index.search(np.array(query_embedding), top_k)

        # ----------------------------------
        # 📚 Collect results
        # ----------------------------------
        results = []
        for i in indices[0]:
            if i < len(chunks):
                results.append(chunks[i])

        return "\n\n".join(results)

    except Exception as e:
        print("❌ SEARCH ERROR:", str(e))
        return ""