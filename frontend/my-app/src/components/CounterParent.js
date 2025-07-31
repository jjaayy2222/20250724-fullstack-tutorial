// 20250724-fullstack-tutorial/frontend/my-app/src/components/CounterParent.js

// React와 useState 훅을 불러옴
import React, { useState } from 'react';


// 자식 컴포넌트: 버튼만 담당, 파일 분리 없이 바로 정의 
/* 함수형 컴포넌트 
- 함수명 ChildCounter, 인자 onIncrement
- 부모 컴포넌트가 줄 어떤 함수가 있다면 버튼의 onClick와 연결해서 사용한다는 의미
- 예상 호출 모습: <ChildCounter onIncrement={() => setCount(count + 1)} />
- onIncrement() = `props`로 받은 콜백 함수(외부에서 넘겨준 함수)
- 즉, 버튼이 클릭되면 `props`로 받은 `onIncrement()` 함수를 실행시킴 */ 
function ChildCounter({ onIncrement, label, value }) {
    return(
        <div>
            <button onClick={onIncrement}>{label}</button>
            <p>현재값: {value}</p>
        </div>
    )
}


// 부모 컴포넌트: 상태(count)를 가지고 있고 자식에게 전달
// 상태 공유 부모
function CounterParent() {
    const [count, setCount] = useState(0);                          // 상태는 오직 부모가 관리

    return (
        <div style={{ border: '1px solid gray', padding: '12px', marginTop: '20px' }}>
            <h2>공유 카운트: {count}</h2>                               {/* 부모가 기억하는 카운트상태 */} 

            {/* 자식에게 상태 변경 함수(onIncrement)를 props로 전달 */}
            {/* 증가, 감소 버튼 만들기 및 라벨 부여 */}
            <ChildCounter onIncrement={() => setCount(count + 1)} label="+1" />
            <ChildCounter onIncrement={() => setCount(count - 1)} label="-1"/>
        </div>
    );
}

export default CounterParent;

// next step = "이벤트, 입력 상태" (InputExample.js)