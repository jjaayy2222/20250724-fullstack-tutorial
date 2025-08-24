// frontend/chatbot-app/src/components/StepStats.js  

import React from 'react';
import { useAppContext } from '../contexts/AppContext';
import './StepStats.css';

const StepStats = () => {
    // 전역 상태에서 통계 정보 가져오기
    const { stepStats } = useAppContext();

    return (
        <div className="step-stats">
            <h3>📊 Step 사용 통계</h3>
            <div className="stats-grid">
                <div className="stat-item">
                    <span className="stat-icon">🏠</span>
                    <span className="stat-label">홈</span>
                <span className="stat-count">{stepStats.home}번</span>
            </div>
                <div className="stat-item">
                    <span className="stat-icon">🏗️</span>
                    <span className="stat-label">Step 1-4</span>
                    <span className="stat-count">{stepStats['step1-4']}번</span>
                </div>
                <div className="stat-item">
                    <span className="stat-icon">📝</span>
                    <span className="stat-label">Step 5</span>
                    <span className="stat-count">{stepStats.step5}번</span>
                </div>
            </div>
        </div>
    );
};

export default StepStats;