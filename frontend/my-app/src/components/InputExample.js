// 20250724-fullstack-tutorial/frontend/my-app/src/components/InputExample.js

import React, { useState } from 'react';                        // React와 useState 훅 임포트

function InputExample() {                                       // InputExample 컴포넌트 정의 시작
                                                                // name: 사용자 입력 텍스트 상태 저장
                                                                // setName: name 상태 변경 함수
  const [name, setName] = useState('');                         // 초기값으로 빈 문자열 설정

  return (                                                      // 컴포넌트 화면 구성 반환
    <div style={{ padding: '16px', marginTop: '20px', border: '1px solid #ccc' }}>
        {/* 제목 표시 */}
        <h2>입력 예제</h2> 

        {/* 사용자 입력 필드 */}
        <input
            type="text"                                         // 입력 타입 텍스트 지정
            value={name}                                        // 입력 필드 값으로 name 상태 연결 (제어 컴포넌트)
            onChange={(e) => setName(e.target.value)}           // 입력값 변경 시 name 상태 업데이트
            placeholder="이름을 입력하세요"                         // 입력 필드 가이드 텍스트
        />

        {/* name 상태에 따른 조건부 환영 메시지 출력 */}
        {/* name 값이 있을 때만 메시지 표시 */}
        {name && <p>환영합니다, <strong>{name}</strong>님!</p>} 
    </div>
  );                                                            // 컴포넌트 화면 구성 반환 끝
}

export default InputExample;                                    // InputExample 컴포넌트 외부로 내보내기

// next stet :