# Children's Artwork Analysis

## 프로젝트 설명
아동 그림 데이터를 분석하여 객체 탐지 모델을 개발했습니다. Detectron2를 활용해 주요 패턴을 도출하고 결과를 시각화했습니다.

## 주요 기술
- 데이터 수집: Open API, 크롤링
- 객체 탐지 모델: Detectron2
- 데이터 시각화: Gradio

## 주요 성과
- 데이터 분석 정확도 90% 이상 향상
- 학습 성능 15% 개선
- 분석 결과를 기반으로 연구팀에 유의미한 인사이트 제공

## 실행 방법
1. **데이터 준비**: `data/` 폴더에 아동 그림 데이터 업로드
2. **모델 학습**: `python train_detectron2.py`
3. **결과 시각화**: `python visualize_results.py`

## 사용 기술 및 도구
- Python, Detectron2, Gradio