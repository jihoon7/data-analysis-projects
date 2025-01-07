# Artwork Object Detection

## 프로젝트 설명
YOLOv8 모델을 사용하여 객체 탐지 모델을 개발했습니다. 회사 데이터가 없기 때문에 프로젝트 내부에서 이미지를 생성하고, 전처리부터 학습, 평가, 시각화까지 모든 단계를 설계했습니다.

## 주요 기술
- 데이터 생성: Python (PIL, OpenCV)
- 객체 탐지 모델: YOLOv8
- 결과 시각화: Matplotlib

## 주요 성과
- 데이터 생성 및 객체 탐지 워크플로우 자동화.
- YOLOv8 모델을 사용한 객체 탐지 정확도 향상.
- 테스트 데이터에서 모델 성능 평가 및 결과 시각화 완료.

## 실행 방법
1. **데이터 생성**: 데이터 생성 스크립트를 실행하여 데이터를 준비합니다.
   ```bash
   python src/data_generation.py
2. 모델 학습: YOLOv8 모델 학습을 실행합니다.
   python src/train_model.py
3. 평가 및 시각화: 테스트 데이터를 평가하고 결과를 시각화합니다.
   python src/evaluate_and_visualize.py

사용 기술 및 도구
- Python, YOLOv8, PIL, OpenCV, Matplotlib
