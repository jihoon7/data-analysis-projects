# PCB Defect Detection

## 프로젝트 설명
PCB 이미지 데이터를 기반으로 YOLOv8을 활용하여 결함 탐지 모델을 개발했습니다. 제조 공정 자동화를 목표로 데이터 생성, 전처리, 학습, 테스트 및 시각화를 포함한 전체 워크플로우를 구현했습니다. 

## 주요 기술
- 데이터 생성: 랜덤 결함 데이터 및 라벨 생성
- 데이터 전처리: 이미지 크기 조정 및 정규화
- 객체 탐지 모델: YOLOv8
- 평가 및 시각화: 모델 예측 결과를 테스트 데이터로 시각화

## 주요 성과
- 모델 학습 및 평가 자동화
- 데이터 생성 및 전처리 워크플로우 확립
- 테스트 데이터로부터 예측 결과 시각화

## 실행 방법
1. **데이터 생성**: 
    ```bash
    python src/data_creation.py
    ```
2. **데이터 전처리**: 
    ```bash
    python src/data_preprocessing.py
    ```
3. **모델 학습**: 
    ```bash
    python src/train_model.py
    ```
4. **모델 평가 및 시각화**: 
    ```bash
    python src/evaluate_model.py
    ```

## 사용 기술 및 도구
- Python, YOLOv8
- OpenCV, PIL
- Matplotlib