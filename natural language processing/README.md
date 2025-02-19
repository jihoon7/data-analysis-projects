# 프로젝트명: 데이터 분석 프로젝트

## 개요
이 프로젝트는 자연어 처리(NLP) 및 데이터 분석을 수행하는 것을 목표로 합니다. `natural language processing` 폴더 내부에 분석 스크립트와 데이터가 포함됩니다.

## 폴더 구조
```
data-analysis-projects/
│── natural language processing/  # NLP 관련 파일 보관
│   │── src/                      # Python 코드 저장
│   │   ├── auto.py               # 자동 NLP 분석 코드
│   │   ├── manual.py             # 수동 NLP 분석 코드
│   │── data/                      # 원본 데이터 폴더 (Git 제외)
│   │── results/                   # 분석 결과 저장 폴더
│   │── config.yaml                 # 설정 파일
│   │── requirements.txt            # 필요한 패키지 목록
│   │── .gitignore                  # Git 제외 파일 목록
│   │── README.md                   # 프로젝트 설명서
```

## 실행 방법
1. **환경 설정**
   ```bash
   pip install -r requirements.txt
   ```
2. **설정 파일 수정**
   - `config.yaml`에서 설정을 필요에 맞게 수정

3. **Python 실행**
   - 자동 NLP 분석 실행
     ```bash
     python src/auto.py
     ```
   - 수동 NLP 분석 실행
     ```bash
     python src/manual.py
     ```

## 주의사항
- `data/` 폴더는 민감한 데이터를 포함하므로 Git에 추가되지 않도록 `.gitignore` 설정이 적용되었습니다.
