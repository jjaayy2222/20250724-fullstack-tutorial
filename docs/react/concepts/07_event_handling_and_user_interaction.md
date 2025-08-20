# 📘 Chapter 7. 이벤트 처리와 사용자 상호작용

## 🔹 `클래스 컴포넌트`에서 이벤트 핸들러 사용하기

### 📌 왜 `바인딩(binding)`이 필요할까?

* 클래스 컴포넌트에서 메서드(함수)를 그냥 쓰면 `this`가 뭔지 모름.
* 그래서 `this`가 컴포넌트 자신을 가리키게 **`바인딩`** 해줘야 함.

### ✅ 예제 코드

```jsx
class Button extends React.Component {
  constructor(props) {
    super(props);

    // handleClick이 this(Button)를 제대로 가리키도록 바인딩
    this.handleClick = this.handleClick.bind(this);
  }

  handleClick(event) {
    console.log('Button clicked');
  }

  render() {
    return <button onClick={this.handleClick}>Click me</button>;
  }
}
```

### 📌 무슨 뜻?

* `constructor` = 컴포넌트가 처음 만들어질 때 실행되는 부분.
* `bind(this)` = `this`가 컴포넌트를 가리키게 해주는 코드.

---

## 🔹 함수형 컴포넌트에서 이벤트 핸들러 사용하기

* 함수형 컴포넌트는 `this`를 `사용하지 않기 때문에` **바인딩할 필요가 없음**
* 그냥 **함수** 하나 만들고 **이벤트에 연결하면 끝!**

### ✅ 예제 코드

```jsx
function Button(props) {
  function handleClick(event) {
    console.log('Button clicked');
  }

  return <button onClick={handleClick}>Click me</button>;
}
```

### 📌 이렇게도 활용 가능 (주의 필요!)

```jsx
function Button(props) {
  return <button onClick={() => console.log('Button clicked')}>Click me</button>;
}
```

* 위 방법은 간단하지만, **렌더링될 때마다 새로운 함수가 생겨서 성능에 안 좋을 수 있음**
* 그래서 함수를 따로 빼서 쓰는 것을 권장

---

## 🎯 React에서 자주 쓰는 이벤트 종류

| 이벤트 종류   | 설명                    | 예시 이벤트                       |
| -------- | --------------------- | ---------------------------- |
| 마우스 이벤트  | 마우스로 클릭하거나 움직일 때      | `onClick`, `onMouseOver`     |
| 키보드 이벤트  | 키보드를 누를 때             | `onKeyDown`, `onKeyUp`       |
| 폼 이벤트    | 입력창에서 값이 바뀔 때         | `onChange`, `onSubmit`       |
| 포커스 이벤트  | 입력창에 커서가 들어가거나 나갈 때   | `onFocus`, `onBlur`          |
| 터치 이벤트   | 스마트폰 같은 터치기기에서 터치할 때  | `onTouchStart`, `onTouchEnd` |
| 드래그 이벤트  | 요소를 드래그할 때            | `onDrag`, `onDrop`           |
| 클립보드 이벤트 | 복사, 잘라내기, 붙여넣기 할 때    | `onCopy`, `onPaste`          |
| 합성 이벤트   | 한국어/일본어 같이 조합 글자 입력 시 | `onCompositionStart`         |
| 휠 이벤트    | 마우스 휠로 스크롤할 때         | `onWheel`                    |

---

## 📊 클래스 컴포넌트 vs 함수형 컴포넌트 - 이벤트 처리 차이

| 항목             | 클래스 컴포넌트                          | 함수형 컴포넌트                    |
| -------------- | --------------------------------- | --------------------------- |
| this 바인딩 필요 여부 | 필요함 (`bind(this)` 사용해야 함)         | 필요 없음                       |
| 이벤트 핸들러 작성 방법  | 클래스 메서드로 작성                       | 그냥 함수로 작성                   |
| 이벤트 핸들러 연결 방법  | `JSX`에서 메서드 사용 (`this.handleClick`) | `JSX`에서 함수 사용 (`handleClick`) |
| 성능 최적화 주의사항    | 바인딩을 `constructor`에서 한번만 하면 됨       | `JSX` 안에서 화살표 함수 사용 지양        |

---