// frontend/chatbot-app/src/components/ThemeToggle.js

import React from 'react';
import { useAppContext } from '../contexts/AppContext';
import './ThemeToggle.css';

const ThemeToggle = () => {
    // 전역 상태에서 테마 정보 가져오기
    const { theme, toggleTheme } = useAppContext();

    return (
        <button 
            onClick={toggleTheme} 
            className={`theme-toggle ${theme}`}
        >
            {theme === 'light' ? '🌙 다크모드' : '☀️ 라이트모드'}
        </button>
    );
};

export default ThemeToggle;
