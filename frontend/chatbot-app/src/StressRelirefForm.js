// frontend/chatbot-app/src/StressReliefForm.js
import React, { useState } from 'react';
import './StressRelirefForm.css';                            // 스타일 파일 불러오기

// StressReliefForm 컴포넌트 정의
const StressReliefForm = () => {
    // 상태(state) 정의: 기분과 계획을 각각 상태로 관리
    const [mood, setMood] = useState('');
    const [plan, setPlan] = useState('');

    // 폼 제출 시 실행되는 함수
    const handleSubmit = (e) => {
        e.preventDefault();                                 // 폼 기본 동작(페이지 새로고침) 방지
        alert(`오늘 기분: ${mood}, 계획: ${plan}`);            // 입력된 값 알림창으로 출력
        setMood('');                                        // 입력 필드 초기화
        setPlan('');
    };

    return (
        // 폼 요소 정의 및 제출 이벤트 처리
        <form className="stress-relief-form" onSubmit={handleSubmit}>
            {/* 기분 입력 필드 */}
            <input 
            type="text"
            placeholder="오늘 기분은?"                              // 입력 안내 텍스트
            value={mood}                                        // 상태 mood와 연결
            onChange={(e) => setMood(e.target.value)}           // 입력값 변경 시 상태 업데이트
            className="input-field"                             // CSS 클래스 지정
            />
        
            {/* 계획 입력 텍스트 영역 */}
            <textarea 
            placeholder="코딩 후 기분 전환 계획은?"                       // 입력 안내 텍스트
            value={plan} // 상태 plan과 연결
            onChange={(e) => setPlan(e.target.value)}               // 입력값 변경 시 상태 업데이트
            className="textarea-field"                              // CSS 클래스 지정
            />

            {/* 제출 버튼 */}
            <button type="submit" className="submit-button">
            기분 UP! 🎯
            </button>
        </form>
    );
};

export default StressReliefForm;                                    // 컴포넌트 내보내기
