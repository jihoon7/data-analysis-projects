# PCB Defect Detection

## 프로젝트 설명
PCB 이미지 데이터를 기반으로 YOLOv5와 SSD를 사용해 결함 탐지 모델을 개발했습니다. 제조 공정 자동화를 목표로 데이터 라벨링과 모델 학습을 수행했습니다.

## 주요 기술
- 데이터 라벨링: Polygon 및 Rectangle 방식
- 객체 탐지 모델: YOLOv5, SSD

## 주요 성과
- 모델 정확도 95% 달성
- 제조 공정 오류율 20% 감소
- 데이터 라벨링 최적화로 팀 작업 시간을 30% 절감

## 실행 방법
1. **데이터 준비**: `data/` 폴더에 PCB 이미지 업로드
2. **라벨링 실행**: `python labeling_tool.py`
3. **모델 학습**: `python train_yolov5.py`

## 사용 기술 및 도구
- Python, YOLOv5, SSD