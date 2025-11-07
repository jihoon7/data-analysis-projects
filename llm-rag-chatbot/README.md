# LLM 기반 사내 휴가·복지 안내 챗봇 (RAG 구조)

### 프로젝트 개요
회사 내부 규정 문서를 기반으로 의미 기반 검색을 수행하는 챗봇 프로젝트입니다.  
Streamlit을 통해 질문을 입력하면 문서에서 유사한 문단을 찾아 답변을 제공합니다.  

GPT API 연동 모듈(`rag_gpt.py`)을 추가해, 필요 시 생성형 답변(Generation)까지 확장할 수 있도록 설계했습니다.

---

## 주요 기능
- **문서 기반 검색 (RAG)**: 문장 단위 임베딩 + 의미 유사도 검색  
- **Streamlit 인터페이스**: 브라우저에서 간단하게 사용 가능  
- **GPT 연동 구조**: OpenAI API를 통해 자연스러운 대화형 응답 확장 가능  
- **ChromaDB 사용**: 로컬 벡터 저장소를 활용해 빠르고 독립적인 검색 가능  
- **Prompt 분리 구조**: 시스템/사용자 프롬프트를 따로 관리해 유지보수 편리

---

## 폴더 구조
llm-rag-chatbot/
│
├── README.md
├── config.yaml
├── app.py
├── test_loader.ipynb
├── data/
│ └── vacation_welfare_policy.txt
├── modules/
│ ├── document_loader.py
│ ├── vectorizer.py
│ ├── query_engine.py
│ ├── rag_gpt.py
│ ├── prompt_templates.py
│ └── init.py
└── vector_store/

---

## ⚙️ 기술 스택

| 구분 | 내용 |
|------|------|
| **언어** | Python 3.10 |
| **임베딩 모델** | jhgan/ko-sroberta-multitask |
| **DB** | ChromaDB |
| **UI** | Streamlit |
| **LLM (선택)** | OpenAI GPT (gpt-4o-mini, gpt-3.5-turbo) |
| **환경 관리** | python-dotenv, config.yaml |

---

## RAG 구조 요약

문서 로드 → 문장 임베딩 → ChromaDB 저장
↓
질문 입력
↓
의미 유사도 기반 검색
↓
관련 문단 출력 + (GPT 응답)

## 실행 방법

1. **필수 패키지 설치**
```bash
pip install -r requirements.txt

2. 문서 임베딩 실행
python test_loader.ipynb

3. Streamlit 실행
streamlit run app.py