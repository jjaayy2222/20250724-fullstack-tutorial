// 20250724-fullstack-tutorial/frontend/my-app/src/components/Counter.js

// React와 useState Hook 불러오기
import React, { useEffect, useState } from 'react';

// useEffect 경고문 없애기
// import만 하고 아직 사용하지 않았을 경우에 뜨는 경우 
/*
function Demo() {
    const [value, setValue] = useState(0);

    // useEffect 사용 예
    useEffect(() => {
        console.log('현재 값:', value);
    }, [value]);

    return (
        <button onClick={() => setValue(value + 1)}>{value}</button>
    );
} */

// Counter 컴포넌트 정의
function Counter() {
    // count: 현재 값 저장 (초기값은 0)
    // setCount: count 값을 변경해주는 함수
    const [count, setCount] = useState(0);

    /* 상태 감지 및 변화 메시지 표시 - useEffect
    - 목표: 상태가 바뀔 때마다 콘솔 or 텍스트로 메시지를 보여주기
    - 도입 이유: React가 “상태가 변했구나!”를 감지하는 훅 개념 이해 */
    useEffect(() => {
        console.log('→ count 변경됨! 현재 값:', count);
    }, [count]);

    // 컴포넌트가 반환할 화면 구성 JSX
    return (
    <div>
        {/* 현재 상태 값 출력 */}
        <h1>현재 값: {count}</h1>

        {/* ver.1 -상태 증가 버튼 */}
        {/* 버튼 클릭 시 count 값 +1 */}
        {/* <button 
                onClick={() => setCount(count + 1)}
                disablde={count >= 10}
            >
                +1 증가
            </button> */}
        {/* 상태 감소 버튼 */}
        {/* <button 
                onClick={() => setCount(count - 1)}
                disabled={count <= 0}
            >
                -1 감소
            </button> */}

        {/* ver.2 - 조건부 상태 관리 */}
        {/* if문 - 상태 최대, 최소값 제한 걸어보기 */}
        {/* disabled = 버튼 비활성화*/}
        <button
            onClick={() => {
                if (count < 10) setCount(count + 1);
            }}
            disabled={count >= 10}
        >
            +1 (최대 10)
        </button>

        <button
            onClick={() => {
                if (count > 0) setCount(count - 1);
            }}
            disabled={count <= 0}
        >
            -1 (0 이하 불가)
        </button>

        {/* 여기에 최대값 도달 메시지를 추가 */}
        {count === 10 && <p style={{color: 'red'}}>최대값에 도달했습니다!</p>}

    </div>
    );
}




// 외부에서 이 Counter 컴포넌트를 사용할 수 있도록 export
export default Counter;

// next step = Lifting State Up(CounterParent.js)