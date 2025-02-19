# 부동산 데이터 기반 AI 챗봇 프로젝트
이 프로젝트는 OpenAPI를 활용하여 부동산 시장 데이터를 분석하고 AI 챗봇을 구현하는 프로젝트입니다.

## 📌 주요 기능
- KB부동산 데이터를 실시간으로 수집
- FAISS + BM25 Hybrid 검색 적용
- OpenAI API를 활용한 질문-응답 시스템
- FastAPI 기반의 AI 챗봇 서버 구축

## 🛠 사용 기술
- Python, Pandas, LangChain, FAISS, OpenAI API, FastAPI

## 🚀 실행 방법
1. 환경 설정 (`pip install -r requirements.txt`)
2. FastAPI 실행 (`uvicorn main:app --reload`)
