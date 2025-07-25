import React, { useState, useEffect } from 'react';

// config.js 파일 대신 여기에 BACKEND_URL을 직접 정의
// 백엔드 API의 기본 URL = Django 서버가 실행될 주소
export const BACKEND_URL = 'http://127.0.0.1:8000/'; 

// Home 컴포넌트를 정의 -> Next.js에서 pages/index.js는 기본적으로 이 이름의 컴포넌트를 내보냄
const Home = () => {
    const [data, setData] = useState('');
  // 'data' = 백엔드에서 가져온 데이터를 저장할 상태 변수
  // 'setData' = 'data' 변수를 업데이트하는 함수 / 초기값은 빈 문자열('')

  // useEffect 훅은 컴포넌트가 마운트(화면에 처음 렌더링)될 때 또는 특정 값(빈 배열 [])이 변경될 때 실행됨
  // 여기서는 빈 배열([])을 사용하여 컴포넌트가 처음 로드될 때만 한 번 실행되도록 설정
    useEffect(() => {
      // 백엔드 API로부터 데이터 가져오기
      // 백틱(`)을 사용하여 JavaScript 변수(BACKEND_URL)를 문자열 안에 쉽게 삽입
      // '/api/hello' = 백엔드에서 정의할 API 엔드포인트
        fetch(`${BACKEND_URL}api/hello`)
            .then((response) => response.json()) // 서버 응답을 JSON 형식으로 파싱(변환)
            .then((data) => setData(data));     // 파싱된 JSON 데이터를 'data' 상태 변수에 저장하여 UI를 업데이트
    }, []); // 의존성 배열. 비어있으면 컴포넌트 마운트 시 한 번만 실행


    
    // 컴포넌트의 JSX(JavaScript XML)를 렌더링
    return (
        <div>
            {/* 환영 메시지 제목 */}
            <h1>Welcome to Fine-Tuning Chatbot!</h1> 
            {/* 백엔드에서 가져온 데이터를 표시합니다. */}
            <p>{data}</p>
        </div>
    );
};

// Home 컴포넌트를 이 파일의 기본 내보내기로 설정
// Next.js는 이 파일을 페이지로 인식하여 해당 컴포넌트를 렌더링함
export default Home;

