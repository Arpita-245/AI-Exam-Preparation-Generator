from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

# Load embedding model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Store embeddings + texts
texts = []
index = None


def create_index(note_texts):
    global texts, index

    texts = note_texts

    embeddings = model.encode(texts)
    dimension = embeddings.shape[1]

    index = faiss.IndexFlatL2(dimension)
    index.add(np.array(embeddings))


def search(query, k=3):
    query_embedding = model.encode([query])

    distances, indices = index.search(np.array(query_embedding), k)

    results = [texts[i] for i in indices[0]]

    return results