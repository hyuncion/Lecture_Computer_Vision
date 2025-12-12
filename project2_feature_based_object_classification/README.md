# Project 2: Feature-Based Object Classification

본 프로젝트는 컴퓨터비전개론 수업의 두 번째 과제로,  
이미지에서 **특징(feature)을 직접 설계하고**,  
간단한 거리 기반 분류기를 이용하여 **객체를 분류**하는 것을 목표로 합니다.

딥러닝이나 고수준 머신러닝 프레임워크를 사용하지 않고,  
영상처리 기법과 통계적 특징을 기반으로 한 분류 과정을  
**NumPy 중심으로 직접 구현**하였습니다.

---

## 📌 Problem Definition

- 분류 대상: **귤(orange)** vs **곶감(dried persimmon)**
- 관찰 가설:
  - 귤은 표면이 거칠어 **에지(edge)가 많음**
  - 곶감은 상대적으로 표면이 매끄러움
- 따라서 Sobel filter 결과의 **표준편차(std)**를 특징으로 사용

---

## 🧩 Code Structure & Roles

### 1️⃣ `prepare_dataset.py`  
**(Dataset Preparation)**

- 원본 이미지들을 학습에 적합한 형태로 변환
- RGB → Grayscale 변환
- 픽셀 값 정규화
- 학습용 이미지 저장

📌 분류를 수행하지 않고, **데이터 정리만 담당하는 전처리 스크립트**

---

### 2️⃣ `sobel_mdc_classifier.py` ⭐  
**(Main Classification Pipeline)**

Project 2의 **핵심 코드**로, 보고서의 모든 실험 결과는 이 스크립트를 기반으로 합니다.

#### 처리 흐름
1. Image slicing (중앙 영역 crop)
2. Grayscale 변환
3. Sobel filter 적용 (x, y 방향)
4. Gradient magnitude 계산
5. Feature extraction: **표준편차(std)**
6. Classifier: **MDC (Minimum Distance Classifier)**

- 학습 이미지: 28장
- 테스트 이미지: 2장
- 평균 feature 벡터와의 거리 기반 분류

📌 “복잡한 모델보다 **적절한 feature 설계가 중요함**”을 보여주는 코드입니다.

---

### 3️⃣ `region_growing_experiment.py`  
**(Experimental Segmentation Approach)**

- Region Growing 기반 이미지 분할(segmentation)을 실험적으로 구현
- 픽셀 밝기 차이를 기준으로 영역 병합
- 가장 큰 영역을 선택하여 객체 분리 시도

📌 대안적 접근에 대한 **실험용 코드**

---

### 4️⃣ `RegionGrowingSample.py`  
**(Algorithm Practice / Reference Code)**

- Region Growing 알고리즘을 독립적으로 구현한 샘플 코드
- 알고리즘 이해를 위한 연습 및 참고 목적

---

## 🔄 Overall Pipeline

```text
Input Image
   ↓
Image Slicing (중앙 영역)
   ↓
Grayscale Conversion
   ↓
Sobel Edge Detection
   ↓
Feature Extraction (Std)
   ↓
Minimum Distance Classifier
   ↓
Class Prediction (귤 / 곶감)
```

---

## 📊 Results (Summary)
- 단일 feature(std) 기반의 간단한 분류기(MDC)로도 유의미한 분류 성능을 확인
- Region Growing은 가능성이 있으나 데이터 규모 대비 계산량이 커 비효율적이었음

---

## 🛠 Implementation Notes
- OpenCV 기반 고수준 분류/머신러닝 API는 사용하지 않음
- Feature 추출 및 분류 로직은 직접 구현
- Classifier: Minimum Distance Classifier (MDC)

---

## 🧠 What I Learned
- “모델보다 feature 설계가 중요해지는 상황”을 직접 경험
- Sobel edge 기반 통계량(std)이 texture 차이를 반영할 수 있음을 확인
- segmentation(Region Growing) 접근은 성능 이전에 계산 효율성 고려가 중요함을 학습
