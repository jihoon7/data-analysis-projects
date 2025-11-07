import os
import chromadb
from sentence_transformers import SentenceTransformer

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
VECTOR_DB_PATH = os.path.join(BASE_DIR, "vector_store")

client = chromadb.PersistentClient(path=VECTOR_DB_PATH)
collection = client.get_or_create_collection(name="docs")

model = SentenceTransformer("jhgan/ko-sroberta-multitask")

def search_similar_chunks(query: str, top_k: int = 3, max_distance: float = 0.95):
    """
    문장 임베딩 후 의미적으로 유사한 문단 검색
    """
    query_vec = model.encode(query).tolist()
    results = collection.query(query_embeddings=[query_vec], n_results=top_k)

    docs = results.get("documents", [[]])[0]
    distances = results.get("distances", [[]])[0]

    if not docs:
        return []

    # 거리 기반 필터링
    filtered = [doc for doc, dist in zip(docs, distances) if dist <= max_distance]

    # 만약 다 걸러졌다면 상위 1개라도 반환
    if not filtered and docs:
        filtered = [docs[0]]
    return filtered
