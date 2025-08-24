# `chatbot-app` 네비게이션 & 컴포넌트 구조화 안내

## **🌟 구조 변경 목표**
- **컴포넌트 분리 및 구조화** (Step1to4.js, Step5.js 분리)
- **네비게이션 시스템 구축** (버튼으로 Step간 이동)
- **상태 관리** (현재 활성 Step 추적)
- **재사용 가능한 구조** 설계

## **🔧 이후 `Step 6` 구현 계획**

### **📁 이후 파일 구조:**

- 
    ```markdown
    ../src/
        ├── App.js              # 메인 네비게이션 + 라우팅
        ├── App.css             # 전체 스타일
        ├── components/
        │   ├── Step1to4.js     # 기존 카운터 + 할일 리스트
        │   ├── Step1to4.css
        │   ├── Step5.js        # 스트레스 해소 폼 (기존)
        │   ├── Step5.css
        │   └── Step6.js        # 새로운 기능 (미래 확장)
        └── ...
    ```

### **🎯 이후 `Step 6` 구현 순서:**

- **components 폴더 생성**
- **Step1to4.js 컴포넌트 분리**: 기존 App.js 내용 이전 및 파일명 변경
- **Step5.js 및 css 생성**: `components` 폴더
- **App.js 네비게이션 구조**: 구현 및 안내
- **Step간 전환 버튼** 추가
