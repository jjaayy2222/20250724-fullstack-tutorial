# 📘 Chapter 3. React 컴포넌트 요약

---

## 💡 핵심 개념

-   **컴포넌트란?**
    -   UI의 일부를 담당하는 **재사용 가능한 코드 조각**
    -   일종의 '함수'처럼 입력(`props`)을 받아 **화면에 출력**
    -   여러 컴포넌트를 조합해서 큰 UI를 완성 (레고 블록처럼)

---

## ⚙️ 컴포넌트의 종류

### ✨ 함수형 컴포넌트

-   **가장 단순·간결**한 정의 방식
-   함수로 정의, `props`(입력 데이터)를 받아 **React 요소 반환**
-   `Hooks`(`useState`, `useEffect` 등)를 사용해 상태와 로직 관리
    ```jsx
    function Welcome(props) {
      return <h1>Hello, {props.name}</h1>;
    }
    ```

### 🏛️ 클래스 컴포넌트

-   ES6 `class`로 정의
    -   `React.Component`를 확장한 클래스로 선언 ➡️ `render()` 메서드를 포함해야 함
-   상태(`state`)와 생명주기(`lifecycle`) 메서드 관리에 유리 (구버전 스타일)
    ```jsx
    class Welcome extends React.Component {
      render() {
        return <h1>Hello, {this.props.name}</h1>;
      }
    }
    ```

---

## 🟢 언제 어떤 컴포넌트를 쓸까?

| **함수형 컴포넌트** | **클래스 컴포넌트** |
| :--------------------------------------------------- | :---------------------------------------------------------- |
| 코드가 **더 직관적**·간단함                         | 복잡한 기능(에러 경계 등) 필요 시 사용/레거시 호환              |
| **Hooks** 활용 (`useState`, `useEffect`, `useContext` 등) | 생명주기 메서드로 복잡한 상태 관리/레거시 프로젝트                  |
| `props` 전달받아 렌더링하는 컴포넌트를 생성하는 경우         | `componentWillMount`, `componentWillUpdate`, `componentWillReceiveProps` 같은 라이프사이클 메서드 필요 시 |
| 최근 React 개발의 **표준** | 점점 사용 빈도 감소 (**권장하지 않음**, 호환용)                   |

-   실무에서는 대부분 **함수형 컴포넌트 + Hooks** 방식이 표준
-   라이프사이클 메서드 향후 React 버전에서 폐기 예정 ➡️ 기존 코드베이스에서는 여전히 클래스 컴포넌트가 일반적이므로 이해 필요

---

### 🟠 클래스 컴포넌트 생명주기 (Lifecycle)

![React 컴포넌트의 라이프사이클](<../images/react_img/class_components_lifecycle.png>)

-   **마운팅(Mounting):** 컴포넌트의 인스턴스가 생성되고 DOM에 삽입될 때
    -   `constructor` ➡️ `static getDeriveStateFromProps()` ➡️ `render` ➡️ `componentDidMount`
-   **업데이트(Updating):** `props`/`state` 변경으로 다시 렌더링될 때
    -   `static getDerivedStateFromProps()` ➡️ `shouldComponentUpdate` ➡️ `render` ➡️ `getSnapshotBeforeUpdate()` ➡️ `componentDidUpdate`
-   **언마운팅(Unmounting):** DOM에서 제거될 때
    -   `componentWillUnmount`

---

-   ❗ React 16.3부터 일부 라이프사이클 메서드 폐기 ➡️ 새로운 메서드 도입
    -   **폐기**: `componentWillMount()`, `componentWillReceiveProps()`, `componentWillUpdate()` 메서드
    -   **도입**: `getDerivedStateFromProps()`, `getSnapshotBeforeUpdate()` 메서드
-   ❗ 함수 컴포넌트(`useState`, `useEffect` `Hook`을 사용하여 생성된 컴포넌트)의 라이프사이클과 클래스 컴포넌트의 라이프사이클 메서드는 다름

---

### 🟩 함수형 컴포넌트와 React Hooks

-   **Hooks:** 함수형 컴포넌트에서 **상태와 다양한 기능**을 쉽게 쓸 수 있게 해주는 함수 (React 16.8에서 도입)
    -   `useState`
        -   함수형 컴포넌트에 **상태 추가**
        -   초기 상태를 인수로 받고 **현재 상태**와 상태를 **업데이트하는 함수**로 구성된 **배열**을 반환

        ```js
        const [count, setCount] = useState(0);      // count = 현재 상태, setCount = 상태 업데이트 함수
        ```

    -   `useEffect`
        -   이전 클래스 컴포넌트의 `componentDidMount`, `componentDidUpdate`, `componentWillUnmount` 라이프사이클 메서드와 같은 역할
        -   첫 번째 렌더링을 포함해 **모든 렌더링 이후에 실행됨**
        -   `side effect`(마운트/업데이트/언마운트 등) 처리

        ```js
        useEffect(() => {
          // 작업...
        }, [의존성]);                                 // useEffect() 기본 구조
        ```

        ```js
        useEffect(() => {
            document.title = `You clicked ${count} times`;
        }, [count]);                                // useEffect Hook은 count 상태가 변경될 때마다 문서 제목을 업데이트
        ```

    -   `useContext`
        -   컴포넌트를 `Context.Consumer`로 감싸지 않고도 컨텍스트의 값을 액세스할 수 있게 함
        -   깨끗하고 가독성 높은 코드 작성 가능

        ```js
        const theme = useContext(ThemeContext);     // theme = ThemeContext의 현재 값을 갖게 됨
        ```

    -   `useRef`
        -   **`.current` 속성을 가진 변경 가능한 객체 생성**
        -   DOM 노드에 직접 액세스 또는 추가 렌더링 없이 값의 지속성 유지에 도움

        ```js
        const inputRef = useRef(null);
        inputRef.current.focus();                   // 컴포넌트가 마운트될 때 입력 요소에 초점을 맞추기 위해 사용
        ```

    -   `useReducer`
        -   **`useState`의 대체 방법**
        -   복잡한 상태 로직 또는 다음 상태가 이전 상태에 의존하는 경우에 유용

        ```js
        const [state, dispatch] = useReducer(reducer, initialArg, init);
                                // reducer함수, 초기 인수, 선택적 초기화 함수를 인수로 받은 useReducer
        // 현재 상태 + 디스패치 메서드와 결합된 배열 반환 ↲
        ```

---

## 📊 표로 정리 (핵심 요약)

| 구분              | 특징/설명                                | 예시                          |
| :---------------- | :--------------------------------------- | :---------------------------- |
| **함수형 컴포넌트** | 간단, Hooks 가능, 최신 표준              | `function App(props) {...}` |
| **클래스 컴포넌트** | class 기반, 생명주기, 레거시 호환            | `class App extends ... {}`    |
| **Props** | 입력값 (부모→자식 전달)                    | `<MyComp name="Jay"/>`        |
| **State** | 내부 데이터(변경 가능), `set` 함수 필요      | `useState`, `this.state`      |
| **Hooks** | 상태/로직 **재활용 함수** | `useState`, `useEffect`       |
| **생명주기** | Mount/Update/Unmount 과정                | `componentDidMount`, etc.     |
| **사용 권장** | **Functions + Hooks(최신)**, Class(구프로젝트) |                               |


### 🧩 비유로 이해하기

-   **컴포넌트:** 레고 하나하나
-   **함수형/클래스형:** 레고 설계 방식 (새로운/옛날)
-   **Props:** 레고 조각에 동봉된 라벨 (입력 정보)
-   **State:** 레고 조각 내에서 바뀔 수 있는 색상이나 움직임
-   **Hooks:** 쉽게 레고에 기능 (불빛, 움직임 등)을 추가하는 스위치