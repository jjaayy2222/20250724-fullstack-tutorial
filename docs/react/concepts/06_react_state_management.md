# 📘 Chapter 6. React에서의 상태 관리

---

## 🔹 상태(State)의 개념 💡

-   **컴포넌트의 내부 데이터 (변경 가능)** = **`UI`에 변경을 줄 수 있는 앱의 부분**
    -   시간에 따라 바뀌는 컴포넌트 내부의 데이터
    -   어떤 컴포넌트 내에서 갖고 있는 숫자, 문자열, ON/OFF 같은 값
            > 🌱 비유: `state` **≒** **`React 컴포넌트의 기억력`** 같은 것

    -   사용자 입력, 네트워크 응답, 시간 흐름, 앱 데이터 변경을 트리거할 수 있는 다른 요소에 의해 변경됨

    -   컴포넌트에 의해 완전히 제어되는 **비공개(`private`) 값 ≠** `props`
        -   ❗ `props` = 읽기 전용 = 변경 가능
        -   `props`는 **외부에서 주는 읽기 전용 값**, `state`는 **내부에서 바꾸는 값**

            > 🌱 비유: `props`는 부모가 주는 도시락 🍱, `state`는 내가 직접 만든 주먹밥 🍙 — 필요에 따라 바꿀 수 있음!

- 🧾 **`props`** 🆚 **`state`**

<table style="border-collapse: collapse; width: 80%; margin: 0 auto;">
  <thead>
    <tr>
      <th style="border: 2px solid #ccc; padding: 10px; width: 20%;"></th>
      <th style="border: 2px solid #ccc; padding: 10px; width: 40%;"><code>props</code></th>
      <th style="border: 2px solid #ccc; padding: 10px; width: 40%;"><code>state</code></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="vertical-align: top; padding: 10px; border: 2px solid #ccc;"><strong>출처</strong></td>
      <td style="vertical-align: top; padding: 10px; border: 2px solid #ccc;">부모 컴포넌트</td>
      <td style="vertical-align: top; padding: 10px; border: 2px solid #ccc;">자기 자신</td>
    </tr>
    <tr>
      <td style="vertical-align: top; padding: 10px; border: 2px solid #ccc;"><strong>변경 요인</strong></td>
      <td style="vertical-align: top; padding: 10px; border: 2px solid #ccc;">부모가 바꿈</td>
      <td style="vertical-align: top; padding: 10px; border: 2px solid #ccc;">자기 자신이 바꿈 (<code>useState</code>)</td>
    </tr>
    <tr>
      <td style="vertical-align: top; padding: 10px; border: 2px solid #ccc;"><strong>역할</strong></td>
      <td style="vertical-align: top; padding: 10px; border: 2px solid #ccc;">외부에서 받아오는 데이터</td>
      <td style="vertical-align: top; padding: 10px; border: 2px solid #ccc;">내부에서 스스로 기억하는 값</td>
    </tr>
    <tr>
      <td style="vertical-align: top; padding: 10px; border: 2px solid #ccc;"><strong>예시 코드</strong></td>
      <td style="vertical-align: top; padding: 10px; border: 2px solid #ccc;">
        <pre style="font-size: 0.8em;"><code class="language-jsx">
function Hello(props) {
  return &lt;h1&gt;Hello, {props.name}!&lt;/h1&gt;;
}


// 사용 예시:
// &lt;Hello name="John!" /&gt;
        </code></pre>
      </td>
      <td style="vertical-align: top; padding: 10px; border: 2px solid #ccc;">
        <pre style="font-size: 0.8em;"><code class="language-jsx">
import { useState } from 'react';

function Counter() {
  const [count, setCount] = useState(0);                      // count = 기억하는 숫자

  return (
    &lt;div&gt;
      &lt;h1&gt;{count}&lt;/h1&gt;
      &lt;button onClick={() => setCount(count + 1)}&gt;+1&lt;/button&gt;
    &lt;/div&gt;
  );
}
        </code></pre>
      </td>
    </tr>
    <tr>
      <td style="vertical-align: top; padding: 10px; border: 2px solid #ccc;"><strong>코드 설명</strong></td>
      <td style="vertical-align: top; padding: 10px; border: 2px solid #ccc;">
        <p>- <code>props.name</code>을 통해 부모 컴포넌트에서 <strong>"John"라는 값을 외부로부터 받아와</strong> 사용</p> 
        <p>- 이 값은 <code>Hello</code> <strong>컴포넌트 내부에서 직접 변경 불가</strong></p>
      </td>
      <td style="vertical-align: top; padding: 10px; border: 2px solid #ccc;">
        <p>- 초기값 = <strong><code>count</code>=0</strong></p>
        <p>- ➡️ <strong>버튼 누르기 = <code>setCount(cont +1)</code> 실행 </strong></p>
        <p>- ➡️ 값이 올라감 ➡️ <strong>React가 자동으로 렌더링</strong></p>        
      </td>
    </tr>
  </tbody>
</table>


## 🔹 클래스 컴포넌트의 상태 설정 방식 자세히 알아보기 🏛️

```jsx
class Counter extends React.Component {
  constructor(props) {
    super(props);
    this.state = { count: 0 };                                  // 초기값 설정
  }

  incrementCount = () => {
    this.setState({ count: this.state.count + 1 });             // 반드시 setState로만 수정
  };

  render() {
    return (
      <div /* div 태그입니다 */>
        <h1 /* h1 태그입니다 */>{this.state.count}</h1>
        <button /* button 태그입니다 */ onClick={this.incrementCount}>증가</button>
      </div>
    );
  }
}
````

  - `state`는 `constructor`에서 초기화
  - 변경은 항상 `this.setState()` 메서드를 사용
  - 변경 시 자동으로 컴포넌트 재렌더링

-----

## 🔹 함수형 컴포넌트 - `useState Hook` 자세히 알아보기 🎣

```jsx
import React, { useState } from 'react';

function Counter() {
  const [count, setCount] = useState(0);                    // 딱 한줄로 state 생성 및 초기화 가능 

  return (
    <div /* div 태그입니다 */>
      <h1 /* h1 태그입니다 */>{count}</h1>
      <button /* button 태그입니다 */ onClick={() => setCount(count + 1)}>증가</button>
    </div>
  );
}
```

  - `useState`는 초기값을 받고 **`[값, 변경함수]`** 쌍 반환
  - `setCount(값)` 호출 시 화면 자동 업데이트

> 🌱 비유: `useState`는 “스마트 리모컨” 📺: 버튼 누르면 상태(`count`)가 바뀌고, TV 화면(렌더) 자동 갱신\!

-----

## 🔹 클래스 컴포넌트 🆚 함수 컴포넌트

|                           | 클래스 컴포넌트                 | 함수 컴포넌트                                                   |
| :------------------------ | :---------------------------| :----------------------------------------------------------- |
| 생성 | **공식 절차(`setState`)** 와 구조(**생성자**) 필요 |  `useState` ➡️ **한 줄에 상태 선언·변경 다 가능** |
| 초기값 설정 | **생성자에서 한 번만** | `useState`의 인수로 바로 가능 |
| 상태 선언 방식 | `this.state = { ... }` | `const [state, setState] = useState()` |
|             | **클래스 내부 `constructor()`에서 `this.state={...}` = 초기값** | **`const [값, 바꾸는 함수] = useState(초기값)`** |
| 상태 변경 방식 | **반드시 `this.setState({...})` 메서드만 가능** | `setState(새값)` **(set함수 호출)** |
|             | = **직접 `state` 수정 금지** | = **2번째로 반환된 `set함수` 값만 변경** |
| 비유 | 마치 “하루 일지장”에다가 오늘의 기분을 적고,기분을 바꿀 땐 무조건 ‘공식 스티커(setState)’를 붙여야 ‘새 기록’이 갱신됨 | **카운터 탁상 달력**에서 한 장씩 넘기는 건 `setCount`, 언제든 0일(초기값)부터 시작해 쉽게 리셋 가능 |
| 코드 길이 | 상대적으로 길고 복잡 | 훨씬 짧고 심플 |
| 현대 개발 트렌트 | 점점 사라지는 추세 | 표준, 실무, 신규 ➡️ 거의 모두 채택 |


-----

## 🔹 상태 끌어올리기 (Lifting State Up) ⬆️

- 개념:
  - 상태를 **공통 부모 컴포넌트로 이동시켜 여러 자식이 공유할 수 있도록 만드는 방법**
  - 여러 컴포넌트가 같은 정보를 써야 하면 그 정보를 위에 있는 부모 컴포넌트 하나가 관리하고 자식들에게 값과 행동을 전달하는 방식
      > 🌱 비유: 여러 버튼이 있고, 각 버튼을 누르면 숫자가 올라가는 상황, 숫자는 각 버튼이 갖고 있으면 따로따로 작동할 것! 
      > 따라서 부모 쪽에서 숫자를 한 번만 기억하고, 🕹️ 버튼은 “올려줘!” 하고 요청만 하는 구조로 만들면 상태가 공유됨 

- 예시 코드:
```jsx
import React, { useState } from 'react'; // useState import 추가

function Counter({ onIncrement }) {
  return <button /* button 태그입니다 */ onClick={onIncrement}>증가</button>;
}

function CounterParent() {
  const [count, setCount] = useState(0);

  return (
    <div /* div 태그입니다 */>
      <h1 /* h1 태그입니다 */>{count}</h1>
      <Counter onIncrement={() => setCount(count + 1)} />
      <Counter onIncrement={() => setCount(count + 1)} />
    </div>
  );
}
```
  - `CounterParent`가 상태(`count`)를 보유
  - 자식(`Counter`)은 버튼 역할만 수행 + 콜백 전달받음
  - 자식은 상태를 몰라도 부모의 상태를 바꿀 수 있음

    | 개념               | 설명                                                                                                |
    | :---------------- | :------------------------------------------------------------------------------------------------- |
    | **상태 끌어올리기**   | 컴포넌트 간 공유가 필요한 상태를 **가장 가까운 공동 부모 컴포넌트로 이동시켜 관리**하는 패턴                            |
    | **적용 위치**       | 공통 부모 컴포넌트(**함수형/클래스형 모두 가능**)에서 상태를 보유하고 **자식**에 **`props`로 전달**                   |
    | **자식 컴포넌트**    | 상태 값을 **직접 관리하지 않고**, 받은 props와 이벤트 **콜백으로 부모 상태 변경 요청**                              |
    | **효과**           | **상태 동기화, 데이터 불일치 방지, 관리 용이성 향상**                                                         |

-----

## 🧾 최종 요약 표 📊

| 항목                      | 설명                                                                                                |
| :------------------------ | :-------------------------------------------------------------------------------------------------- |
| **상태 (State)** | 컴포넌트 내부에서 관리되는 값, 시간/사용자/이벤트 등에 따라 변경됨                                  |
| **클래스 컴포넌트에서 상태** | `this.state`로 저장, `this.setState()`로 변경                                                       |
| **함수형 컴포넌트에서 상태** | `useState` 훅 사용 → `[값, 변경함수]` 반환                                                            |
| **상태 변화 후 렌더링 방식** | 상태 변경 → 자동으로 다시 렌더링됨                                                                  |
| **상태 끌어올리기** | 두 자식이 공유해야 할 상태를 부모로 올려서 공유함 (예: `Counter` 컴포넌트와 `CounterParent` 참조) |
| **`props` vs `state`** | `props`: 읽기 전용, 부모 → 자식 전달 / `state`: 변경 가능, 컴포넌트 내부 관리                      |
| **리렌더 트리거 방식** | 상태가 `set`되면 화면 자동 갱신 (`React가 내부에서 감지`)                                             |

