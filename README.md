# 20250724-fullstack-tutorial (Full-stack Tutorial Practice Repository)

- 이 저장소는 **"Pybo - 파이썬 기반 데이터 분석 입문"** 책(Wikidocs: [효율과 성능의 삼위일체: Django Rest Framework, React, Next.js 웹 개발의 진수](https://wikidocs.net/book/9596))을 참고하여 진행하는 풀스택 웹 개발 실습 프로젝트입니다.
- This repository serves as a full-stack web development practice project, referencing the book **"Pybo - Python-based Data Analysis Introduction"** (Wikidocs: [효율과 성능의 삼위일체: Django Rest Framework, React, Next.js 웹 개발의 진수](https://wikidocs.net/book/9596)).

**주요 목적 / Main Purpose**
- 책의 내용을 따라가며 백엔드(Django, Django REST Framework) 및 프론트엔드(Next.js) 개발 기술을 학습하고 실습하는 데 중점을 둡니다.
- The primary focus is on learning and practicing backend (Django, Django REST Framework) and frontend (Next.js) development technologies by following the book's content.

**참고 사항 / Please Note**
* 이 프로젝트는 **지속적으로 업데이트**될 예정입니다. 다만, 업데이트 일정은 명확하게 정해져 있지 않습니다.
* This project is subject to **ongoing updates**. However, there is no fixed update schedule.

* 학습 과정에서 **참고하는 교재 및 GitHub 저장소의 내용과 다소 차이가 있을 수 있습니다.** 이는 학습자의 이해와 프로젝트 진행 상황에 따라 최적의 방법을 모색하거나, 추가적인 기능을 구현하기 위함입니다.
* During the learning process, there **may be slight deviations from the referenced book and its associated GitHub repository.** This is done to explore optimal approaches based on the learner's understanding and project progress, or to implement additional features.

---
## 참고 / Reference
* [효율과 성능의 삼위일체: Django Rest Framework, React, Next.js 웹 개발의 진수](https://wikidocs.net/book/9596)
* [Git-Hub](https://github.com/Eirene-dev/book_trininity)

---
## 프로젝트 개요 / Project Overview
* **BE**: Django, Django REST Framework를 활용한 API 서버 구축
* **FE**: React, Next.js를 활용한 웹 애플리케이션 개발

---
## 진행 상황 / Current Progress
-   Django 프로젝트 생성 및 설정
    -   Django 앱(myapp) 생성 및 기본 뷰/템플릿 연동
-   Django REST Framework 설치 및 API 뷰 구성
    -   Django project 구조 재조정 (backend / django-practice ➡️ myproject)
  -   DRF API 문서화 (drf-spectacular) 및 설정 개선
    -   DRF API 기본 페이지네이션 적용
  -   Django 템플릿 경로 설정 문제 해결 및 테스트 페이지 추가
  -   DRF 'Book' 모델 API 테스트 코드 구현 및 결과 검증
    -   pyenv, Poetry로 파이썬 환경 재설정
  -   REST API로 ChatGPT 모델을 Fine-Tuning 하기
    - Model 업데이트: FineTunedModel과 TrainingData 요소 추가
    - Serializers 업데이트: Model 요소 추가에 따른 코드 변경
    - Admin 업데이트:
    - Django Shell로 데이터 추가
    - API 접근, Auth Token 설정: 테스트 완료 ➡️ 슈퍼유저 및 토큰 생성, API 접속 확인
    - REST API ➡️ 학습 데이터 추가 및 보기 구현
    - GEMINI API 사용 ➡️ Fine-tuning
- **React_기본**
  - **React 기본 사항: 구성 요소, 상태 및 Props**
      - **개념 정리 ➡️ `../docs/react`, `../docs/images` 디렉토리, `01_react_concept.md` 파일 생성**
  - **React 프로젝트 설정**
      - **개념 정리 : `02_setting_react_project.md`**
      - **프로젝트 생성 및 실습**
          - **`/frontend/my-app/'**
          - **`01_create-react0app.md`**


---
**개발 환경 / Development Environment:**
-   Python 3.13.5
-   Django 5.2.4
-   Django REST Framework 3.16.0
-   Node.js v22.17.1
-   Next.js next@15.4.4
-   React 19.1.0
-   pyenv
-   Poetry