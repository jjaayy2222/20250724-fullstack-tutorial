# 📘 Chapter 8. 조건부 렌더링과 리스트

> `React`에서는 상태나 조건에 따라 화면에 보여줄 내용을 바꾸거나, 
> 
> 배열을 반복해서 여러 개의 컴포넌트를 만들 수 있음
> 
> 이런 걸 잘 이해하면 더 똑똑한 웹앱을 만들 수 있음

---

## ✅ 조건부 렌더링 (Conditional Rendering)

* `상황`(`조건`)에 따라 **다른 컴포넌트를 보여주는 것**
  * 예를 들어, 사용자가 **로그인했는지 안 했는지**에 따라 다른 인사말을 보여줄 수 있음

### 예시 코드

```jsx
function UserGreeting(props) {
  return <h1>Welcome back!</h1>;  // 로그인한 사용자
}

function GuestGreeting(props) {
  return <h1>Please sign up.</h1>; // 로그인 안 한 사용자
}

function Greeting(props) {
  const isLoggedIn = props.isLoggedIn;

  if (isLoggedIn) {
    return <UserGreeting />;
  }
  return <GuestGreeting />;
}

// false면 GuestGreeting이 보임
ReactDOM.render(
  <Greeting isLoggedIn={false} />,
  document.getElementById('root')
);
```

### 💡 핵심 포인트

* `isLoggedIn`이 `true`면 로그인 환영 인사 (`UserGreeting`)
* `false`면 가입 권유 인사 (`GuestGreeting`)
* `JavaScript`의 `if` 문을 사용해서 **조건을 판단**

---

## ✅ 리스트 렌더링 (배열 반복해서 컴포넌트 만들기)

* `배열`을 이용해서 여러 개의 요소를 화면에 나타낼 수 있음
* 자바스크립트의 `map()` 함수를 자주 사용

### 예시 코드

```jsx
function NumberList(props) {
  const numbers = props.numbers;

  const listItems = numbers.map((number) =>
    <li>{number}</li>
  );

  return (
    <ul>{listItems}</ul>
  );
}

const numbers = [1, 2, 3, 4, 5];

ReactDOM.render(
  <NumberList numbers={numbers} />,
  document.getElementById('root')
);
```

### 💡 핵심 포인트

* `numbers.map(...)` → `배열`을 `하나씩 반복`하며 `<li>` 요소를 만듦
* `JSX` 안에서는 중괄호 `{}`로 자바스크립트 코드를 사용 가능

---

## ✅ 키(`key`) 속성 사용하기

* 리스트를 만들 때는 **각 항목이 고유하게 식별**될 수 있도록 `key`를 꼭 넣어줘야 함
* `React`가 어떤 항목이 추가되거나, 변경되었는지 알아보기 쉽게 도와줌

### 예시 코드

```jsx
function NumberList(props) {
  const numbers = props.numbers;

  const listItems = numbers.map((number) =>
    // key 사용 → 숫자값을 문자열로 바꿔서 사용할 수 있게 됨
    <li key={number.toString()}>
      {number}
    </li>
  );

  return (
    <ul>{listItems}</ul>
  );
}

const numbers = [1, 2, 3, 4, 5];

ReactDOM.render(
  <NumberList numbers={numbers} />,
  document.getElementById('root')
);
```

### 💡 핵심 포인트

* `key={number.toString()}` : `숫자값`을 `문자열`로 바꿔서 `key`로 사용
* `key`는 **형제 요소들 사이에서만 고유**하면 됨
  * 꼭 전 세계적으로 고유할 필요는 없음
* `고유한 ID가 없을 땐` `index`를 `key`로 쓸 수도 있지만, **비추천**
  **→ 순서가 바뀌면 성능 문제 생길 수 있음**

---

## 📊 정리표: 조건부 렌더링 vs 리스트 렌더링

| 항목        | 조건부 렌더링               | 리스트 렌더링                     |
| --------- | --------------------- | --------------------------- |
| 목적        | `조건`에 따라 다른 내용을 보여줌     | `배열`로 여러 요소를 `반복`해서 보여줌         |
| 자주 쓰는 문법  | `if`, `? :` 삼항연산자     | `map()` 함수                  |
| 예시        | 로그인 상태에 따라 인사말 다르게 표시 | 숫자 리스트를 `<li>`로 보여주기        |
| `key` 필요 여부 | ❌ 필요 없음               | ✅ 필요함 (`항목마다 고유한 key 지정`해야 함) |
| 주로 쓰는 상황  | 로그인/로그아웃, 버튼 클릭 등     | 목록 출력, 테이블, 리스트 카드 등        |

---
