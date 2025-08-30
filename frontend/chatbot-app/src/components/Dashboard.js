// src/components/Dashboard.js

import React, { useEffect } from 'react';
import { useNavigate, useLocation } from 'react-router-dom'; // ← 추가 및 수정
import { useAppContext } from '../contexts/AppContext';
import Step5 from './Step5';
import ThemeToggle from './ThemeToggle';
import './Dashboard.css';

const Dashboard = () => {
  const { incrementStepCount } = useAppContext();
  const navigate = useNavigate();  // ← 추가
  const location = useLocation();  // ← 추가

  // 페이지가 로드될 때마다 Step 5의 카운트를 증가시킴
  useEffect(() => {
    // 현재 경로가 dashboard일 때만 실행
    if (location.pathname !== '/dashboard') {
      incrementStepCount('step5');
    }
  }, [incrementStepCount, location.pathname]);            // ← location 추가

  return (
    <div className="dashboard-container">
      <h2 className="dashboard-title">🎛️ 대시보드</h2>
      
      <div className="control-panel">
        <ThemeToggle />
        <button 
          className="control-btn" 
          onClick={() => navigate('/settings')}  // ← 클릭 이벤트 추가
        >
          ⚙️ 설정
        </button>
        <button 
          className="control-btn"
          onClick={() => navigate('/stats')}     // ← 클릭 이벤트 추가
        >
          📊 통계
        </button>
      </div>
      
      <div className="dashboard-content">
        <div className="widget">
          <h3 className="widget-title">📋 Form Controls</h3>
          <Step5 />
        </div>
      </div>
    </div>
  );
};

export default Dashboard;
