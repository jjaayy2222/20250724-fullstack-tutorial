// frontend/chatbot-app/src/contexts/AppContext.js
import React, { createContext, useContext, useState } from 'react';

// 1. Context 생성 (전역 상태 저장소 만들기)
const AppContext = createContext();

// 2. Provider 컴포넌트 (상태를 제공하는 역할)
export const AppProvider = ({ children }) => {
    // 전역으로 관리할 상태들
    const [user, setUser] = useState({
        name: 'Jay',                                    // 사용자 이름
        email: 'jay@example.com'                        // 사용자 이메일
    });

    const [theme, setTheme] = useState('light');        // 테마 (light/dark)

    const [stepStats, setStepStats] = useState({
        'step1-4': 0,                                    // Step 1-4 사용 횟수
        'step5': 0,                                      // Step 5 사용 횟수
        'home': 0                                        // 홈 방문 횟수
    });

    // 테마 변경 함수
    const toggleTheme = () => {
        setTheme(prevTheme => prevTheme === 'light' ? 'dark' : 'light');
    };

    // Step 사용 횟수 증가 함수
    const incrementStepCount = (stepName) => {
        setStepStats(prev => ({
            ...prev, // 기존 상태 유지 (spread 문법)
            [stepName]: prev[stepName] + 1 // 해당 Step만 +1
        }));
    };

    // 사용자 정보 업데이트 함수
    const updateUser = (newUserInfo) => {
        setUser(prev => ({ ...prev, ...newUserInfo }));
    };

    // 모든 컴포넌트에서 사용할 값들
    const contextValue = {
        // 상태 값들
        user,
        theme, 
        stepStats,
        // 상태 변경 함수들
        updateUser,
        toggleTheme,
        incrementStepCount
    };

    return (
        // Provider로 감싸서 하위 컴포넌트들이 상태를 사용할 수 있게 함
        <AppContext.Provider value={contextValue}>
            {children}
        </AppContext.Provider>
    );
};

// 3. Context를 쉽게 사용할 수 있는 커스텀 Hook
export const useAppContext = () => {
    const context = useContext(AppContext);
    if (!context) {
        throw new Error('useAppContext는 AppProvider 내부에서만 사용 가능합니다!');
    }
    return context;
};
