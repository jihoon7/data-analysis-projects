from pathlib import Path
import re

def load_documents(directory: str, chunk_size: int = 200):
    """
    data 폴더 내 txt 파일을 문장 단위로 분할하여 반환
    """
    chunks = []
    for file in Path(directory).glob("*.txt"):
        with open(file, "r", encoding="utf-8") as f:
            text = f.read().replace("\n", " ")

        # 문장 단위 분리
        sentences = re.split(r'(?<=[.!?])\s+', text)
        for sent in sentences:
            sent = sent.strip()
            if len(sent) > 10:
                chunks.append((file.stem, sent))
    return chunks
