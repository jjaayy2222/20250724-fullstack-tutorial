# 📘 Chapter 9. React 개발을 위한 모범 사례

* 주요 내용

| **항목**            | **올바른 방법**                       | **잘못된 방법**                     |
| ----------------- | -------------------------------- | ------------------------------ |
| **컴포넌트 크기**       | 작은 컴포넌트로 한 가지 일만 하도록 분리하기        | 하나의 컴포넌트에 많은 일을 시키기            |
| **단일 책임 원칙(SRP)** | 각 컴포넌트는 하나의 일만 담당하기              | 여러 가지 일을 하는 큰 컴포넌트 사용          |
| **불변성**           | 상태는 직접 수정하지 않고 새로운 복사본을 만들어 사용   | 상태를 직접 수정하기                    |
| **PropTypes 사용**  | `PropTypes`로 데이터 타입과 필수 여부를 검사하기 | 타입 검사를 하지 않고 데이터 타입을 직접 사용하는 것 |
| **파일 구조와 명명 규칙**  | 명확한 이름과 파일 구조 유지하기               | 모호한 이름을 사용하거나 파일 구조가 혼잡한 경우    |

---

## 1. **깔끔하고 모듈식인 React 코드 작성**

* `React`: **깔끔하고 모듈식인 코드**
  * 이렇게 하면 코드를 관리하기 더 쉬워지고, 나중에 수정하기도 편함

## 2. **단일 책임 원칙 (`SRP`)**

* **단일 책임 원칙**은 컴포넌트가 한 가지 책임만 가지도록 만드는 규칙
  * 하나의 컴포넌트가 너무 많은 일을 처리하면, 그 컴포넌트는 관리하기 힘들고 오류가 발생할 확률이 높아짐. 
  * 예시: 로그인 기능을 담당하는 컴포넌트는 로그인만, 환영 메시지를 보여주는 컴포넌트는 환영만 보여줘야 함

<br>

* 컴포넌트를 작게 나누면 **재사용성**과 **가독성**이 좋아짐
  * 나중에 코드를 수정할 때도 실수가 적어지고, 이해하기 쉬워짐


### 잘못된 예시 (SRP 위반 사례)

```jsx
import React, { useState } from 'react';

function UserAccount() {
  const [user, setUser] = useState({ name: '', email: '' });
  const [loggedIn, setLoggedIn] = useState(false);

  const handleChange = (e) => {
    setUser({ ...user, [e.target.name]: e.target.value });
  }

  const handleLogin = () => {
    setLoggedIn(true);
  }

  return (
    <div>
      <input name="name" onChange={handleChange} />
      <input name="email" onChange={handleChange} />
      <button onClick={handleLogin}>Login</button>
      {loggedIn && <h2>Welcome, {user.name}!</h2>}
    </div>
  );
}
```

* `UserAccount` 컴포넌트 
  * `로그인 처리`와 `사용자 정보 관리`를 `동시 담당` 
  * 나중에 수정할 때 어려움이 생길 수 있음

### 좋은 예시 (`SRP 적용`)

```jsx
import React, { useState } from 'react';

function LoginForm({ onLogin }) {               // 로그인 폼만 처리
  const [user, setUser] = useState({ name: '', email: '' });

  const handleChange = (e) => {
    setUser({ ...user, [e.target.name]: e.target.value });
  }

  return (
    <div>
      <input name="name" onChange={handleChange} />
      <input name="email" onChange={handleChange} />
      <button onClick={() => onLogin(user)}>Login</button>
    </div>
  );
}

function WelcomeMessage({ user }) {             // 환영 메시지만 표시
  return <h2>Welcome, {user.name}!</h2>
}

function UserAccount() {                        // 로그인 상태 관리, LoginForm, WelcomeMessage 조정 역할
  const [user, setUser] = useState(null);

  return (
    <div>
      {!user && <LoginForm onLogin={setUser} />}  
      {user && <WelcomeMessage user={user} />}    
    </div>
  );
}

export default UserAccount;
```

* 분리
  * `LoginForm` = 로그인
  * `WelcomeMessage` = 환영만 담당
  * `UserAccount` = 로그인 상태를 관리하고, 두 컴포넌트를 조정하는 역할

<br>

## 3. **함수형 컴포넌트 사용하기**

* `React`에서는 **`함수형 컴포넌트를 더 많이 선호`**
* 이유: 코드가 `간단`하고, `관리`하기 `더 쉬워`지기 때문
  * 함수형 컴포넌트에서는 `useState`와 같은 `React 훅`을 사용해서 상태를 관리 가능

<br>

### 클래스 컴포넌트 예시

```jsx
import React, { Component } from 'react';

class Counter extends Component {
  constructor(props) {
    super(props);
    this.state = { count: 0 };                  // this, bind 필요
  }

  increment = () => {
    this.setState({ count: this.state.count + 1 });    
  }

  render() {
    return (
      <div>
        <p>Count: {this.state.count}</p>
        <button onClick={this.increment}>Increment</button>
      </div>
    );
  }
}

export default Counter;
```

<br>

### 함수형 컴포넌트 예시 (더 간단!)

```jsx
import React, { useState } from 'react';

function Counter() {
  const [count, setCount] = useState(0);        // useState 훅 사용 (this, bind 필요 X)

  const increment = () => setCount(count + 1);

  return (
    <div>
      <p>Count: {count}</p>
      <button onClick={increment}>Increment</button>
    </div>
  );
}

export default Counter;
```

<br>

## 4. **불변성 (`Immutability`)**

* `상태(state)`는 **직접 수정하면 안 됨** 
* **항상 새로운 복사본** 을 **만들어서 수정** → 그 후에 `상태`를 `업데이트`해야 함
* 그래야 `코드`가 `예측 가능`하고 `오류`를 `줄일 수 있음`

### 잘못된 예시

```jsx
class MyComponent extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      myArray: [1, 2, 3]
    };
  }

  handleClick = () => {
    this.state.myArray.push(4);     // 불변성 위반 → 직접 수정하면 안됨
  };

  render() {
    // ...
  }
}
```

### 올바른 예시 (불변성 지키기)

```jsx
class MyComponent extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      myArray: [1, 2, 3]
    };
  }

  handleClick = () => {
    const newArray = [...this.state.myArray];           // 상태 복사하기
    newArray.push(4);
    this.setState({ myArray: newArray });               // 복사한 후 변경하기 
  };

  render() {
    // ...
  }
}
```

* 상태를 `수정할 때는` **항상 새로운 객체나 배열을 만들어서 변경해야 함**

## 5. **React의 코딩 스타일과 규칙 따르기**

* `React`에서는 일관된 코딩 스타일을 따르는 것이 중요
* 코드의 `가독성`, `유지보수성`, `협업 효율성`이 향상

<br>

### **1) 이름 지정 규칙**

  * **컴포넌트 이름**: **파스칼 표기법 (`PascalCase`)** 사용
  
  * **속성(`props`) 이름**: **카멜 표기법 (`camelCase`)** 사용
    * `React`에서는 `PropTypes`를 사용해서 각 컴포넌트가 받는 `props`의 타입 확인 가능 
  
  * 잘못된 타입의 데이터를 넣었을 때, 개발 중에 경고를 받을 수 있음

#### 잘못된 예시

```jsx
function U({ uN, uP }) {
  return (
    <div>
      <img src={uP} alt={uN} />
      <h1>{uN}</h1>
    </div>
  );
}
```

<br>

#### 예시

```jsx
function UserProfile({ userName, userPhoto }) {        // 이름은 의미가 명확하고 설명적이어야 함
  return (
    <div>
      <img src={userPhoto} alt={userName} />  
      <h1>{userName}</h1>
    </div>
  );
}

```

### **2) 파일 구조**

* `React` 프로젝트를 `논리적으로 구성`하면 코드 관리가 수월해짐
* `컴포넌트`들을 `기능`이나 `페이지별`로 디렉토리로 나누는 것이 좋음


#### 예시 파일 구조

```plaintext

/src
  /components
    /Button
      Button.js
    /Header
      Header.js
    /Footer
      Footer.js
  /pages
    /Home
      Home.js
    /About
      About.js
  App.js
  index.js

```

### **3) `PropTypes` 사용**

* `PropTypes` = 컴포넌트에 전달되는 **속성(props)**의 `타입`을 `검사`하는 `도구` 
* 코드에서 잘못된 타입이 전달되었을 때 경고 메시지가 표시됨


#### 예시
```jsx
import React from 'react';
import PropTypes from 'prop-types';

function Greeting(props) {
  return <h1>Hello, {props.name}</h1>;
}

Greeting.propTypes = {
  name: PropTypes.string.isRequired,                // name은 반드시 string, 필수로 제공되어야 함
};

export default Greeting;
```

### **4) `JSX` 구문 사용**

* `JSX` = `JavaScript` 코드 안에 `HTML`과 `유사한 문법`을 `사용`할 수 있게 해줌
* `컴포넌트`를 작성할 때 `코드`가 `더 직관적`이고 `읽기 쉬워짐`

#### 예시
```jsx
function Hello() {
  return <h1>Hello, world!</h1>;
}
```

#### 여러 줄의 JSX 표현식

* `JSX`가 여러 줄로 작성될 때는 괄호로 묶어야 함

* 예시

```jsx
return (
  <div>
    <MyComponent />
  </div>
);
```

### **5) 컴포넌트 크기를 작고 집중적으로 유지**

* 컴포넌트는 가능한 한 `작고 간단하게 유지`해야 함
  * 하나의 컴포넌트가 여러 가지 일을 하게 되면 관리하기 어려워지고, 버그가 생길 가능성도 높아짐
* 대신 `하나의 일`을 잘하는 `작은 컴포넌트들로 나누는 것`이 `좋음`

#### (1) 효율적인 컴포넌트 설계 및 성능 최적화 팁

* `React`는 기본적으로 효율적인 라이브러리지만, 잘못 사용하면 비효율적
* 성능 최적화를 위해 다음과 같은 팁을 따를 수 있습니다:

##### **➀ 불필요한 재렌더링 피하기**

   * `shouldComponentUpdate` 또는 `React.memo()`를 사용하여, 컴포넌트가 필요할 때만 재렌더링 되게 해야 함
   * 상태나 속성(`props`)이 변경되면 컴포넌트가 다시 그려지는데, 이 변경이 실제로 화면에 변화를 일으키지 않으면 재렌더링을 막는 것이 좋음


##### **➁ 리스트 렌더링 시 키 사용**

   * 리스트 항목을 렌더링할 때 `key` 속성을 설정하면, React가 항목을 효율적으로 추적하여 변경 사항만 업데이트

   ```jsx
   const items = ['apple', 'banana', 'cherry'];

   return (
     <ul>
       {items.map((item, index) => (
         <li key={index}>{item}</li>
       ))}
     </ul>
   );
   ```

##### **➂ 컴포넌트의 지연 로딩**

   * `React.lazy()`를 사용하여, 처음 로드할 때 필요하지 않은 컴포넌트는 나중에 로드할 수 있음
   * `페이지 로드 속도를 빠르게 할 수 있음`

   ```jsx
   const OtherComponent = React.lazy(() => import('./OtherComponent'));
   ```

##### **➃ 배포 시 프로덕션 빌드 사용**

   * 개발용 빌드는 디버깅을 돕기 위해 여러 가지 경고와 메시지를 포함하지만, 실제로는 성능을 저하시킴. 
   * 프로덕션 빌드로 배포하여 성능을 최적화해야 함.

##### **➄ 앱의 성능 프로파일링**

   * `React DevTools`에서 제공하는 **Profiler** 기능을 사용하여 앱의 성능을 측정
   * 불필요한 렌더링이 있는 부분을 찾아 개선


---

### 차이점 비교표

| 항목              | 함수형 컴포넌트                                   | 클래스 컴포넌트                            |
| --------------- | ------------------------------------------ | ----------------------------------- |
| **상태 관리**       | `useState` 훅 사용                            | `this.state`와 `this.setState` 사용    |
| **이벤트 핸들러 바인딩** | 바인딩 불필요                                    | 생성자에서 `this` 바인딩 필요                 |
| **코드 간결성**      | 코드가 짧고 간단함                                 | 코드가 길고 복잡함                          |
| **성능**          | 더 효율적이고 가독성이 좋음                            | 메모리 소비가 많고, 성능이 떨어질 수 있음            |
| **사용성**         | React 16.8 이상에서만 가능                        | React 16.8 미만에서만 사용 가능              |
| **기능 확장성**      | `useEffect`, `useContext` 등의 훅을 활용하여 확장 가능 | `componentDidMount` 등 클래스 기반 메서드 활용 |

---