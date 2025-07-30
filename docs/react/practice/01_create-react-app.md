# 📘 Chapter 2. React 프로젝트 생성 (Create React App)

---

## 1. 💻 `Node.js` 및 `npm` 설치 또는 확인

-   설치: 이전에 설치 (README.md 참고)
-   설치 확인하기
    -   `node --version`
    -   `npm --version`

    -   ❗ 설치되어 있지 않다면 [nodejs.org](https://nodejs.org/en)에서 LTS 버전으로 다운로드 & 설치

---

## 2. 🚀 `Create React App`으로 프로젝트 생성

#### (1) ✨ 프로젝트 생성

-   터미널에서 원하는 폴더로 이동
    -   `npx create-react-app my-app`
-   실행 시 `my-app` 폴더 **자동 생성**
-   내부에 **필요한 디렉토리/파일들이 자동 구성** (⏱ 약 1~2분 소요)

#### (2) 📂 프로젝트 디렉토리로 이동 및 구조 확인

-   이동
    -   `cd my-app`
-   `VS Code`로 열기 (선택 사항)
    -   `code .`
    -   ❗ `code` 명령어가 안 된다면: VS Code 내부에서 `Shell Command: Install 'code' command in PATH` 실행 후 재시작

-   구조 확인

    ```
    my-app/
    ├── README.md              # 프로젝트 설명 파일
    ├── node_modules/          # 패키지 설치된 폴더
    ├── package.json           # 프로젝트 정보 & 의존성 관리
    ├── .gitignore             # Git이 무시할 파일 목록
    ├── public/
    │   ├── **index.html** # 앱의 진짜 HTML 뼈대
    │   └── 기타 정적 리소스
    └── src/
        ├── **App.js** # React 컴포넌트 시작점!
        ├── **index.js** # 메인 진입 파일
        └── 기타 CSS, 이미지 등
    ```

#### (3) ▶️ 앱 실행

-   기본 React 환영 페이지 확인
    -   `npm start` ➡️ `http://localhost:3000`에서 브라우저 자동 열림

    -   ![기본 React 환영 페이지](<../images/react_img/기본 React 환영 페이지.png>)

-   🎯 기본 환영 페이지 바꿔보기
    -   `my-app` 기본 구조 확인
    -   `src/App.js` 열기 ➡️ `JSX` 구조 확인
    -   컴포넌트 바꿔보기 ➡️ 예시: “안녕하세요, Jay님!” 출력 등
        -   `src/App.js` 속 `<p>` 태그 바꾸기
        -   ![기본 React 환영 페이지 변경](<../images/react_img/기본 React 환영 페이지 변경.png>)

---