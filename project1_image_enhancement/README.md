# Project 1: Image Enhancement

본 프로젝트는 컴퓨터비전개론 수업의 첫 번째 과제로,  
**노이즈가 심한 이미지를 사람이 인식 가능한 수준으로 개선하는 것**을 목표로 합니다.

이를 위해 강의에서 배운 기초 영상처리 연산들을  
기능별 모듈로 나누어 구현하고, 하나의 처리 파이프라인으로 구성하였습니다.

---

## 📌 Project Overview

Project 1에서는 영상처리의 가장 기본적인 흐름인  
**명암 보정 → 노이즈 제거 → 경계 강조** 과정을 직접 구현하였습니다.

각 단계는 독립적인 Python 파일로 분리되어 있으며,  
최종적으로 하나의 메인 스크립트에서 순차적으로 실행됩니다.

---

## 🧩 File-wise Description

### 1️⃣ `IntensityTransform_st.py`  
**(Intensity Transformation & Preprocessing)**

노이즈 제거 이전 단계에서 이미지의 **밝기 분포와 대비를 조정**하는 전처리 파트입니다.

#### 역할
- 어두운 이미지를 밝게 조정
- 대비가 낮은 이미지를 선명하게 변환

#### 주요 기법
- RGB → Grayscale 변환
- Histogram Equalization
- Z-standardization
- Min–Max Normalization
- Window-level adjustment

📌 필터링 이전에 이미지를 “보기 좋은 상태”로 만드는 핵심 전처리 단계이며,  
특히 **violin 이미지에서 문자 인식이 가능해지도록 만든 핵심 코드**입니다.

---

### 2️⃣ `Smoothing_part.py`  
**(Noise Reduction / Smoothing)**

이미지에 포함된 다양한 형태의 노이즈를 제거하는 파트입니다.

#### 역할
- 랜덤 노이즈 제거
- Salt-and-pepper 노이즈 완화

#### 사용 기법
- Gaussian Filter
- Median Filter

#### 특징
- `clock_noise1`, `clock_noise2` 이미지에 주로 적용
- Mask를 직접 생성하여 convolution 수행
- NumPy 기반 구현

📌 이미지를 부드럽게 만들어 이후 경계 검출이 가능하도록 합니다.

---

### 3️⃣ `Sharpening_part.py`  
**(Sharpening / Edge Enhancement)**

노이즈가 제거된 이미지에서  
**시계 바늘, 물체 윤곽과 같은 중요한 경계(edge)를 강조**하는 파트입니다.

#### 사용 기법
- Laplacian Filter
- Sobel Filter (x, y 방향)
- Gradient magnitude 계산

📌 Project 2의 feature extraction으로도 이어지는 핵심 개념으로,  
“부드러워진 이미지를 다시 또렷하게 만드는 단계”입니다.

---

### 4️⃣ `test.py`  
**(Main Pipeline Script)**

앞선 모든 단계를 하나로 연결하여 실행하는 메인 스크립트입니다.

#### 수행 흐름
1. 이미지 로드
2. Grayscale 변환
3. Intensity Transformation
4. Smoothing
5. Sharpening
6. 결과 이미지 저장

📌 전체 영상처리 파이프라인을 검증하고 결과를 생성하는 역할을 합니다.

---

## 🔄 Image Processing Pipeline

```text
Input Image
   ↓
Intensity Transformation
   ↓
Noise Reduction (Smoothing)
   ↓
Edge Enhancement (Sharpening)
   ↓
Output Image
```

## 🛠 Implementation Overview
- 본 프로젝트는 OpenCV를 사용하지 않고, NumPy와 기본 Python 라이브러리만을 사용하여 구현하였습니다.
- 입력 이미지를 grayscale로 변환한 후 명암 분포를 조정
- Gaussian 및 Median filtering을 통해 다양한 형태의 노이즈 제거
- Laplacian 및 Sobel filter를 사용하여 중요한 경계(edge) 정보 강조
- 처리 순서와 파라미터를 조절하여 최적의 시각적 결과 도출

---

## 🧠 What I Learned
- 영상의 밝기 분포 조정만으로도 가시성이 크게 향상될 수 있음을 이해함
- 노이즈 제거와 경계 강조는 trade-off 관계에 있음을 실험적으로 확인
- 필터의 종류뿐 아니라 **적용 순서가 결과에 큰 영향을 미침**을 학습
- 이후 객체 분류 및 3D 비전으로 확장되는 컴퓨터비전의 기초 역량을 확보함

---

## 📎 Notes
- 본 프로젝트는 교육 목적의 구현입니다.
- 처리 결과는 정량적 성능보다 시각적 개선 효과를 기준으로 평가하였습니다.
