# Computer Vision Projects (Undergraduate)

본 저장소는 컴퓨터비전개론 학부 수업에서 수행한  
**세 개의 프로젝트(Project 1–3)**를 정리한 것입니다.

기초 영상처리부터 객체 분류, 카메라 캘리브레이션까지  
컴퓨터 비전의 핵심 개념을 단계적으로 학습하고 구현하였습니다.

---

## 📁 Project Overview

- **Project 1: Image Enhancement**  
  기초 영상처리 연산을 이용한 명암 보정, 노이즈 제거, 경계 강조

- **Project 2: Feature-Based Object Classification**  
  Sobel 기반 feature 추출과 거리 기반 분류기를 이용한 객체 분류

- **Project 3: Camera Calibration**  
  체스보드 패턴을 이용한 카메라 내부·외부 파라미터 추정

---

## 🖼 Project 1: Image Enhancement

### Goal
노이즈가 심한 이미지를 사람이 인식 가능한 수준으로 개선하는 것을 목표로 한다.

### Key Techniques
- Intensity Transformation  
  - Histogram Equalization  
  - Z-standardization  
  - Min–Max Normalization  
- Noise Reduction  
  - Gaussian Filter  
  - Median Filter  
- Edge Enhancement  
  - Laplacian Filter  
  - Sobel Operator  

### Outcome
- 노이즈 환경에서도 시각적으로 의미 있는 정보 복원
- 영상처리의 기본 연산과 처리 순서에 대한 이해 확립

---

## 🍊 Project 2: Feature-Based Object Classification

### Goal
이미지에서 특징(feature)을 직접 설계하여 객체(귤 / 곶감)를 분류한다.

### Feature & Classifier
- Feature: Sobel edge 결과의 **표준편차(std)**
- Classifier: **Minimum Distance Classifier (MDC)**

### Results
- 단일 feature 기반 분류임에도 약 **90% 정확도** 달성
- Region Growing 기반 segmentation은 계산량 문제로 최종 미채택

### Key Insight
- 모델의 복잡도보다 **feature 설계의 중요성**을 경험

---

## 📷 Project 3: Camera Calibration

### Goal
체스보드 패턴을 이용하여 카메라의 내부 파라미터와 외부 파라미터를 추정한다.

### Experimental Setup
- Chessboard: 7 × 7 corners
- Square size: 13 mm
- Images: 11장 (다양한 위치·방향에서 촬영)

### Results
- Intrinsic matrix 안정적으로 추정
- Reprojection error ≈ **0.96**
- 실제 거리와 비교 시 합리적인 정확도 확인

### Discussion
- 촬영 각도 변화에 따른 extrinsic 파라미터 변화 분석
- 미세한 오차는 카메라 흔들림 및 코너 검출 오차로 판단

---

## 🧠 What I Learned (Overall)

- 기초 영상처리 연산이 고급 비전 문제의 기반이 됨을 이해
- Feature 기반 접근법의 장점과 한계를 명확히 인식
- 2D 이미지와 3D 세계 좌표 간의 수학적 관계 이해
- 컴퓨터 비전 문제에서 정확도와 계산 효율성의 균형 중요성 학습

---

## 📎 Notes

- 모든 프로젝트는 교육 목적의 구현입니다.
