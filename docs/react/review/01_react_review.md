# React

## ✅ React 컴포넌트란?

React에서는 웹사이트를 **블록처럼 쌓아 만들어요.**

* 예를 들어, 쇼핑몰 웹사이트를 만든다고 하면?

  * **헤더(Header)**, **상품 목록(Product List)**, **장바구니(Cart)**, **푸터(Footer)** 이런 것들이 각각 하나의 **컴포넌트**.

📦 컴포넌트는 마치 **레고 블록**처럼 생각하면 됨.

* 레고 블록 하나하나가 컴포넌트!
* 조립하면 웹페이지가 완성돼요!

---

## ✅ 함수형 컴포넌트 vs 클래스형 컴포넌트

React에는 **두 가지 방식**으로 컴포넌트를 만들 수 있음.

### 🎈 함수형 컴포넌트 (쉽고 간단한 방식)

```jsx
function Welcome(props) {
  return <h1>Hello, {props.name}</h1>;
}
```

🧠 비유: 요리는 **간단한 레시피**만 있으면 되는 요리사

* 이름만 받아서 “Hello, 이름”을 보여주는 단순한 컴포넌트
* 별다른 준비물이 필요 없음

### 🧰 클래스형 컴포넌트 (조금 더 복잡한 방식)

```jsx
class Welcome extends React.Component {
  render() {
    return <h1>Hello, {this.props.name}</h1>;
  }
}
```

🧠 비유: **셰프처럼 도구도 많고 레시피도 복잡한 요리사**

* 더 많은 기능을 넣을 수 있지만 코드가 길고 복잡함
* 지금은 별로 안 쓰이지만, 옛날에는 이게 표준이었음

---

## ✅ 상태(state)란?

상태는 **컴포넌트가 기억하는 값**

예시:

```jsx
const [count, setCount] = useState(0);
```

🧠 비유: 게임 캐릭터의 **HP(체력)** 같은 것

* 시간이 지남에 따라 변하고, 그에 따라 화면이 바뀌어요
* `useState`는 함수형 컴포넌트에서 상태를 쓰게 해주는 **도구**

---

## ✅ 라이프사이클(Lifecycle)이란?

컴포넌트도 **살아있는 생명체**처럼 태어나고, 자라고, 죽음.

🧠 비유: 애완동물 키우는 것처럼!

1. **태어날 때** → `componentDidMount()` (처음 한 번 실행)
2. **변화할 때** → `componentDidUpdate()` (업데이트될 때마다 실행)
3. **사라질 때** → `componentWillUnmount()` (죽기 직전 실행)

👉 이런 걸 **클래스형 컴포넌트**에서 다루는 것.

하지만 지금은 `useEffect()` 하나로 대부분 해결 가능!

```jsx
useEffect(() => {
  console.log("컴포넌트가 실행되었어요!");
}, []);
```

---

## ✅ Hooks란?

Hooks는 함수형 컴포넌트를 더 똑똑하게 만들어주는 **비밀무기**!

`React 16.8부터 도입`된 기능.

### 주요 Hooks:

* **`useState`: 상태 저장**
* **`useEffect`: 실행 시점 제어**
* **`useContext`: 전역 데이터 사용**
* **`useRef`: DOM 직접 접근**
* **`useReducer`: 복잡한 상태 관리**

🧠 비유: 요리할 때 쓰는 **도구들**

* 칼, 냄비, 믹서기 등등 → 필요한 도구만 꺼내쓰기!

---

## ✅ 함수형 vs 클래스형 컴포넌트 비교표

| 항목         | 함수형 컴포넌트        | 클래스형 컴포넌트                         |
| ---------- | --------------- | --------------------------------- |
| 코드 길이      | 짧고 간단함 ✨        | 길고 복잡함 😅                         |
| 사용 시기      | 현재 기준 주로 사용됨 👍 | 레거시 코드에서 사용됨                      |
| 상태 사용      | `useState` 훅 사용 | `this.state` 사용                   |
| 라이프사이클     | `useEffect` 사용  | 전용 메서드 사용 (`componentDidMount` 등) |
| 가독성        | 높음 👀           | 낮음 😵                             |
| React에서 권장 | ✅ 사용 권장         | ❌ 새 코드에서는 거의 사용 안 함               |

---

## 요약하면?

* 🧱 **컴포넌트는 레고 블록**
* 🎯 **함수형 컴포넌트는 쉽고 빠르게 개발**
* 🧠 **Hooks는 함수형 컴포넌트를 더 똑똑하게 만들어주는 도구**
* 📜 **클래스형은 과거 방식, 지금은 거의 안 씀**


---
<br>

## ✅ JSX란 뭐야?

### 📦 JSX는 JavaScript + HTML

React에서 사용하는 특별한 언어인데,
**JavaScript 안에 HTML을 쓸 수 있게 해주는 문법**

---

### 🧠 비유로 이해해 보자!

> 📺 "텔레비전을 만드는 레고 블록"을 생각해 보자!

보통 HTML로 만들면:

```html
<h1>Hello</h1>
```

JavaScript로만 만들려면:

```js
document.createElement("h1");
```

근데 JSX를 쓰면:

```jsx
const element = <h1>Hello</h1>;
```

👉 레고 설명서를 HTML처럼 쓰면서, JavaScript처럼 작동하게 도와주는 게 바로 JSX예요!

---

## ✅ JSX를 쓰면 좋은 이유

* 코드를 더 **짧고 예쁘게** 쓸 수 있어요 ✨
* **눈에 보이듯이** HTML처럼 작성할 수 있어서 이해하기 쉬워요
* 실제로는 **JavaScript로 바뀌어서** 작동돼요

---

## ✅ JSX 안에서 JavaScript 쓰는 법

JSX 안에서 **중괄호 `{}`** 를 쓰면 JavaScript 코드도 넣을 수 있어요!

```jsx
const name = "John";
const element = <h1>Hello, {name}!</h1>;
```

👉 출력 결과: **Hello, John!**

---

### 🧠 비유: 마법의 상자 `{}`

중괄호 `{}`는 **마법 상자**.
그 안에 **계산이나 변수**를 넣으면 화면에 그 결과가 뿅 하고 나타남!

```jsx
<h2>{3 + 5}</h2>  // => 8 출력
```

---

## ✅ ReactDOM.render()가 뭐지?

이건 JSX로 만든 내용을 **화면에 보여주는 명령어**.

```jsx
const element = <h1>Hello</h1>;
ReactDOM.render(element, document.getElementById('root'));
```

이 코드는 이렇게 말하는 거랑 같음:

🗣️ "Hey 브라우저야! 저기 `root`라는 공간에 **이 h1 요소**를 보여줘!"

---

## ✅ JSX로 만든 간단한 컴포넌트 예시

```jsx
function App() {
  const name = "John";
  const items = ["Apple", "Banana", "Cherry"];

  return (
    <div>
      <h1>Hello, {name}!</h1>
      <p>This is a paragraph.</p>

      <ul>
        {items.map(item => <li>{item}</li>)}
      </ul>

      <button onClick={() => alert("Button clicked!")}>
        Click me
      </button>

      <input type="text" placeholder="Type something..." />
    </div>
  );
}
```

### 이 코드가 하는 일:

| JSX 코드                        | 실제 역할              |
| ----------------------------- | ------------------ |
| `<h1>Hello, {name}!</h1>`     | 이름을 불러주는 제목        |
| `<ul> {items.map(...)} </ul>` | 과일 목록을 li로 만들어 보여줌 |
| `<button onClick={...}>`      | 클릭하면 알림창 띄우기       |
| `<input type="text" />`       | 텍스트 입력창 만들기        |

---

## ✅ JSX에서 꼭 기억해야 할 점

| JSX 사용법             | 설명                  | 비유                      |
| ------------------- | ------------------- | ----------------------- |
| `className`         | HTML의 `class` 대신 사용 | `class`는 JS에서 이미 쓰고 있어서 |
| `{}`                | JavaScript 표현식 사용   | 마법 상자!                  |
| `onClick={}`        | 클릭 이벤트 처리           | 버튼 누르면 반응하게             |
| `<input />`         | 자기 스스로 닫히는 태그       | 자기 알아서 문 닫는 문!          |
| `ReactDOM.render()` | JSX를 브라우저에 보여주는 함수  | "이거 여기 보여줘!"            |

---

## ✅ 요약 정리 표

| 개념                | 쉬운 설명                 | 예시                               |
| ----------------- | --------------------- | -------------------------------- |
| JSX               | JS 안에 HTML을 쓸 수 있는 문법 | `<h1>Hello</h1>`                 |
| 중괄호 `{}`          | JS 변수나 계산 결과 보여줌      | `{3 + 4}` → 7                    |
| className         | JSX에서 CSS 클래스를 넣는 속성  | `<div className="box">`          |
| onClick           | 버튼 클릭 등의 이벤트 처리       | `<button onClick={...}>`         |
| ReactDOM.render() | JSX를 실제 웹페이지에 보여줌     | `ReactDOM.render(<App />, root)` |

---

## 마무리 ✨

JSX는 React의 핵심 문법이지만
**실제로는 JavaScript로 바뀌어서 작동**한다는 걸 기억하면 됨!

* **HTML처럼 보이지만**
* **JavaScript로 움직이고**
* 화면에는 **진짜 웹페이지**처럼 보이는 마법!

---

## ✅ 요약 + 첨언

| 파일             | 역할                  | 설명                                                                               |
| -------------- | ------------------- | -------------------------------------------------------------------------------- |
| **App.js**     | **JSX 작성 공간**       | 화면에 보여줄 컴포넌트를 구성. HTML처럼 생겼지만 JS 문법을 사용한 JSX 코드가 들어감.                         |
| **index.js**   | **렌더링 시작점**         | App.js에서 만든 내용을 웹 브라우저에 붙이는 역할. (`ReactDOM.createRoot(...).render(<App />)`) |
| **index.html** | **진짜로 보여지는 웹페이지 틀** | `<div id="root"></div>`라는 자리에 App.js의 내용이 표시됨 → 이건 브라우저에서 보는 `실제 HTML`  |

---

## 🧠 흐름을 이미지처럼 그려보면

```
[ App.js ] → JSX로 화면 구성
      ↓
[ index.js ] → App 컴포넌트를 렌더링
      ↓
[ index.html ] → 화면에 실제로 보여짐
```

---

## 🧠 먼저 개념부터 정리: "상태(State)란?"

> 🎮 **React의 상태는, 게임 캐릭터의 체력이나 점수처럼 계속 바뀌는 정보**

* 게임 캐릭터의 `체력`이 100에서 90으로 줄어들면, 화면에 숫자가 바뀜
* 마찬가지로, React 컴포넌트도 내부에 **'상태(State)'** 라는 데이터를 저장하고,
* 그게 바뀌면, **자동으로 화면(UI)이 다시 그려짐!**

---

## 🧪 예시 1: 버튼 누르면 숫자가 올라가는 "카운터 앱"

### 🧑‍🏫 클래스 컴포넌트 방식 (옛날 방식)

```jsx
class Counter extends React.Component {
  constructor(props) {
    super(props);
    this.state = { count: 0 }; // 상태 정의

    this.increment = this.increment.bind(this);
  }

  increment() {
    this.setState({ count: this.state.count + 1 }); // 상태 업데이트
  }

  render() {
    return (
      <div>
        <h1>{this.state.count}</h1>
        <button onClick={this.increment}>+1</button>
      </div>
    );
  }
}
```

🧾 여기서 `this.state.count`는 화면에 보여줄 **숫자 상태**,
`this.setState()`를 호출하면 숫자가 바뀌고 화면도 다시 보여줘요!

---

### ✅ 함수형 컴포넌트 + useState Hook (요즘 방식)

```jsx
import React, { useState } from 'react';

function Counter() {
  const [count, setCount] = useState(0); // 상태 정의

  return (
    <div>
      <h1>{count}</h1>
      <button onClick={() => setCount(count + 1)}>+1</button>
    </div>
  );
}
```

📌 `useState(0)`은 "count라는 상태를 0으로 시작하자!"는 뜻이고,
`setCount()`는 버튼을 누를 때마다 상태를 1씩 올려주는 역할이에요!

---

## 📶 비유로 쉽게 설명해보면…

> 🧃 **React 상태(state)는 텀블러 속 음료수!**

* `state`는 텀블러에 담긴 음료수(변할 수 있는 데이터)
* 우리가 버튼을 누를 때마다 음료 양이 바뀌면,
* `React`가 자동으로 "남은 양"을 보여주는 라벨을 바꿔줌

---

## 🔄 컴포넌트끼리 상태를 공유하고 싶다면?

### ✅ `"상태 끌어올리기"` 기법 사용하기

> 🎈 예: 형제가 있는 집에서 **공용 리모컨을 부모가 들고 있는 느낌**

* 자식 컴포넌트들이 서로 **같은 숫자**를 공유해야 할 때가 있음
* 이럴 땐 각각 상태를 갖는 게 아니라, **부모가 상태를 갖고**
* 자식은 그 상태를 **사용하거나 바꿀 수 있게 props로 전달**받음

---

### 예시: Counter 두 개가 같은 숫자를 공유함

```jsx
function Counter({ onIncrement }) {
  return <button onClick={onIncrement}>+1</button>;
}

function CounterParent() {
  const [count, setCount] = useState(0); // 상태는 부모가 갖고 있음!

  return (
    <div>
      <h1>{count}</h1>
      <Counter onIncrement={() => setCount(count + 1)} />
      <Counter onIncrement={() => setCount(count + 1)} />
    </div>
  );
}
```

🧠 여기서 `Counter`는 버튼을 렌더링만 하고,
진짜 상태(count)는 부모(`CounterParent`)가 관리해요.

---

## 📋 상태 관리 요약 정리표

| 구분                | 설명                                        | 예시               |
| ----------------- | ----------------------------------------- | ---------------- |
| **State(상태)**     | 시간에 따라 바뀌는 데이터                            | 숫자, 입력값, 체크 여부 등 |
| **클래스 컴포넌트에서 상태** | `this.state`로 저장, `this.setState()`로 업데이트 | 옛날 방식            |
| **함수형 컴포넌트에서 상태** | `useState()` 훅 사용                         | 요즘 방식            |
| **상태 끌어올리기**      | 여러 컴포넌트가 같은 데이터를 공유할 때, 부모가 상태를 갖고 자식에 전달 | 공용 리모컨 비유        |
| **상태 바뀌면?**       | 화면이 자동으로 다시 그려짐 (리렌더링)                    | 상태 = UI를 바꾸는 트리거 |

---

## 💬 결론 한 줄 요약

> React에서 \*\*상태(state)\*\*는 **화면에 보여줄 정보**이고,
> 이게 바뀌면 **화면(UI)** 도 자동으로 바뀜 🎉

---

## 🧊 먼저, `Props`가 뭔지부터!

> ### 🎁 **Props는 부모가 자식에게 주는 선물이에요!**

* React에서 컴포넌트 = 하나의 독립된 블록
* 어떤 컴포넌트(부모)가 다른 컴포넌트(자식)에게 **정보를 전달하고 싶을 때**,
  👉 그 정보를 **props**라는 이름으로 넘겨줌

> 마치 부모님이 도시락(데이터)을 싸서 자녀에게 주는 것처럼! 🍱

---

## 🧪 예시: `Greeting`이라는 컴포넌트

```jsx
function Greeting(props) {
  return <h1>Hello, {props.name}</h1>;
}
```

이 컴포넌트를 이렇게 사용할 수 있음:

```jsx
<Greeting name="Alice" />
```

결과는?

```html
<h1>Hello, Alice</h1>
```

* 부모가 `name="Alice"`라는 **props**를 넘겼고,
* 자식 컴포넌트(Greeting)는 그걸 받아서 표시한 것!
* `props.name` = "Alice"

---

## 📶 데이터 흐름 비유: 물은 위에서 아래로 흐른다!

> React의 데이터 흐름 = **단방향(one-way)** 
> 
> 즉, **"부모 ➡️ 자식"** 방향으로만 흐름 ⬇️

* 부모가 데이터를 주고,
* 자식은 그걸 **받기만** 함
* 자식은 그 데이터를 **바꾸지 못함! (읽기 전용)**

📌 **자식이 부모에게 말하고 싶을 때는?**
👉 부모가 자식에게 **함수(props로 전달)** 를 주고,
자식이 **그 함수를 호출해서** 부모에게 알릴 수 있음!

---

## 🎮 예시: 버튼 클릭해서 숫자 증가하기 (부모 자식 협업!)

```jsx
// 자식 컴포넌트
function Child({ count, onIncrement }) {
  return (
    <div>
      <p>현재 숫자: {count}</p>
      <button onClick={onIncrement}>+1</button>
    </div>
  );
}

// 부모 컴포넌트
function Parent() {
  const [count, setCount] = useState(0);

  return (
    <Child 
      count={count} 
      onIncrement={() => setCount(count + 1)} 
    />
  );
}
```

* `count` 숫자는 부모가 관리해요.
* 자식은 버튼을 누르면 부모에게 "숫자 올려줘!"라고 말하는 함수(onIncrement)를 호출해요.

---

## 🕵️‍♀️ 그럼... 이런 질문 생길 수 있어요:

### Q. "props 없이도 자식이 알아서 쓰면 안 돼요?"

❌ 아니에요! 자식 컴포넌트는 다른 컴포넌트의 데이터를 몰라야 해요.
그래야 재사용할 수 있고, 독립적인 블록이 되죠.

---

## ✅ props를 더 안전하게 쓰는 방법

### 1. PropTypes로 유효성 검사

```jsx
Greeting.propTypes = {
  name: PropTypes.string.isRequired
};
```

* `name`은 **반드시 문자열이어야 해!** 라고 알려줌
* 틀리면 개발자 콘솔에 **경고⚠️** 뜸!

### 2. 기본 props 설정하기

```jsx
Greeting.defaultProps = {
  name: "Guest"
};
```

* `name`을 안 줘도 걱정 없어요. 자동으로 `**Guest**`가 들어감

---

## 🧠 Props 요약 정리표

| 항목               | 설명                      | 예시                                 |
| ---------------- | ----------------------- | ---------------------------------- |
| **Props란?**      | 부모 → 자식으로 전달되는 데이터      | `<Greeting name="John" />`         |
| **읽기 전용**        | 자식이 직접 변경할 수 없음         | `props.name = 'James'` ❌           |
| **데이터 흐름**       | 단방향 (부모 ➡️ 자식)          | 위에서 아래로만 전달                        |
| **함수 전달**        | 자식이 부모에게 알리고 싶을 때 사용    | `onClick={handleClick}`            |
| **PropTypes**    | props 타입 확인 (문자열, 숫자 등) | `PropTypes.string.isRequired`      |
| **defaultProps** | props가 없을 때 기본값 지정      | `defaultProps = { name: 'Guest' }` |

---

## 🔚 마무리 요약 한 줄

> **Props는 부모가 자식에게 정보를 주는 선물이고, 자식은 그걸 받아서 화면에 보여주는 역할** 🎁
> 직접 바꿀 수는 없지만, 함수를 통해 부모에게 말은 할 수 있음! 🗣️

---

## 🎯 이벤트가 뭐야?

> **이벤트 = 사용자가 행동했을 때 생기는 일**!

예를 들어:

* 버튼을 클릭했을 때 👉 **onClick 이벤트**
* 키보드를 눌렀을 때 👉 **onKeyDown 이벤트**
* 입력창에 글자를 썼을 때 👉 **onChange 이벤트**

👉 이런 일들이 발생하면, 우리는 **"무슨 일이 일어났을 때 어떤 일을 하자!"** 라는 **함수(=이벤트 핸들러)** 를 만들어서 반응하게 됨

---

## 🎮 비유: 버튼은 게임기 컨트롤러!

* 버튼은 마치 게임기의 🎮 버튼처럼 누르면 뭔가 일이 생겨야 하잖아?
* React에서는 `onClick` 같은 이벤트 속성을 사용해서
  👉 "이 버튼이 눌리면 이 함수를 실행해줘!" 라고 **미리 약속**하는 것!

```jsx
function handleClick() {
  alert("게임 시작!");
}

<button onClick={handleClick}>Start Game</button>
```

* 버튼이 눌리면 `handleClick` 함수가 실행돼서 **"게임 시작!"** 알림이 뜨는 것!

---

## 🏫 클래스 vs 함수형 컴포넌트

### 1. 클래스 컴포넌트: 옛날 방식의 컴포넌트

```jsx
class MyButton extends React.Component {
  constructor(props) {
    super(props);
    this.handleClick = this.handleClick.bind(this);
  }

  handleClick() {
    console.log("Clicked!");
  }

  render() {
    return <button onClick={this.handleClick}>Click</button>;
  }
}
```

### 🔧 왜 바인딩이 필요할까?

> 클래스에서는 `this`가 누구인지를 **잃어버릴 수 있어서** 직접 묶어줘야 해요.

```js
this.handleClick = this.handleClick.bind(this);
```

* 이걸 바인딩이라고 해요. (줄 묶기 같은 거라고 생각하면 돼요)

---

### 2. 함수형 컴포넌트: 요즘 많이 쓰는 방식! 🎉

```jsx
function MyButton() {
  function handleClick() {
    console.log("Clicked!");
  }

  return <button onClick={handleClick}>Click</button>;
}
```

* **함수형에서는 바인딩 필요 없어요!**
* 왜냐하면 `this`가 없고, 함수가 깔끔하니까요. 😎

---

## 💡 이벤트 핸들러 작성 꿀팁

### ❌ JSX 안에 바로 함수를 쓰면?

```jsx
<button onClick={() => console.log("Clicked!")}>Click</button>
```

* 이렇게 써도 되지만, **매번 새 함수가 만들어져서** 성능에 안 좋을 수 있음.
* 렌더링이 자주 일어나면 느려질 수 있음. 😬

### ✅ 미리 함수로 만들어두자!

```jsx
function handleClick() {
  console.log("Clicked!");
}

<button onClick={handleClick}>Click</button>
```

---

## 🧪 어떤 이벤트들이 있을까?

React에서는 진짜 많아요. 대표적인 걸 정리해줄게요:

| 구분      | 이벤트 이름          | 설명             |
| ------- | --------------- | -------------- |
| 💻 마우스  | `onClick`       | 클릭할 때          |
|         | `onDoubleClick` | 더블 클릭할 때       |
|         | `onMouseOver`   | 마우스를 올릴 때      |
| ⌨️ 키보드  | `onKeyDown`     | 키를 누를 때        |
|         | `onKeyUp`       | 키를 뗄 때         |
| ✍️ 입력   | `onChange`      | 입력창에 글자가 바뀔 때  |
|         | `onSubmit`      | 폼 제출할 때        |
| 🧠 포커스  | `onFocus`       | 입력창에 포커스가 생길 때 |
|         | `onBlur`        | 포커스가 사라질 때     |
| 🎞 스크롤  | `onScroll`      | 스크롤할 때         |
| 📱 터치   | `onTouchStart`  | 화면을 터치했을 때     |
| 📋 클립보드 | `onCopy`        | 복사할 때          |
|         | `onPaste`       | 붙여넣기할 때        |

---

## 🎁 전체 흐름 정리 (비유 포함)

| 항목           | 설명                  | 비유                |
| ------------ | ------------------- | ----------------- |
| 이벤트          | 사용자의 행동             | 게임기의 버튼 누르기       |
| 핸들러 함수       | 행동에 반응하는 함수         | 버튼 누르면 점프하게 만들기   |
| 클래스 컴포넌트     | this 때문에 바인딩 필요     | 리모컨 배터리 위치 맞추기    |
| 함수형 컴포넌트     | 바인딩 필요 없음           | 무선 이어폰 자동 연결처럼 간편 |
| JSX 속성       | `onClick`, `onChange` 등 | 버튼에 동작을 설정하는 스위치  |
| 직접 화살표 함수 쓰기 | 되긴 하지만 성능 주의        | 매번 새 건전지 넣는 느낌 ⚠️ |

---

## 🔚 마무리 한 줄 요약

> **React에서 이벤트는 `“무슨 일이 생기면 이렇게 반응해!”`라고 알려주는 리모컨 같은 것**
> 
> 사용자의 행동에 따라 우리가 준비한 함수를 실행시켜주는 것! 🎮