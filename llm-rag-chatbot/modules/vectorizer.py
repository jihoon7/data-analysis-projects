import os
import uuid
import chromadb
from sentence_transformers import SentenceTransformer

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
VECTOR_DB_PATH = os.path.join(BASE_DIR, "vector_store")

client = chromadb.PersistentClient(path=VECTOR_DB_PATH)
collection = client.get_or_create_collection(name="docs")

# 한국어 임베딩 특화 모델
model = SentenceTransformer("jhgan/ko-sroberta-multitask")

def embed_chunks(chunks):
    """문단을 임베딩 후 DB에 저장"""
    for idx, (filename, chunk) in enumerate(chunks):
        emb = model.encode(chunk).tolist()
        collection.add(
            documents=[chunk],
            embeddings=[emb],
            ids=[f"{filename}_{idx}_{uuid.uuid4()}"]
        )
