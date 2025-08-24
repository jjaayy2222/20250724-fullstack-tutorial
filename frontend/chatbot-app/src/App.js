// frontend/chatbot-app/src/App.js
import React, { useState, useEffect } from 'react';
import './App.css';
import { AppProvider, useAppContext } from './contexts/AppContext';
import Step1to4 from './components/Step1to4';
import Step5 from './components/Step5'; 
import UserProfile from './components/UserProfile';
import ThemeToggle from './components/ThemeToggle';
import StepStats from './components/StepStats';

// 실제 App 컴포넌트 (Context를 사용하는 부분)
const AppContent = () => {
  const [currentStep, setCurrentStep] = useState('home');
  
  // 전역 상태 사용하기
  const { theme, incrementStepCount, user } = useAppContext();

  // Step 변경 시 통계 업데이트 + 기존 방식 유지
  const handleStepChange = (stepName) => {
    setCurrentStep(stepName);
    incrementStepCount(stepName);           // 사용 횟수 증가
  };

  // 테마에 따른 CSS 클래스 적용
  useEffect(() => {
    document.body.className = theme;        // body에 테마 클래스 추가
  }, [theme]);

  const renderStepContent = () => {
    switch(currentStep) {
      case 'step1-4':
        return <Step1to4 />;
      case 'step5':
        return <Step5 />; 
      case 'stats':
        return <StepStats />;
      default:
        return (
          <div className="home-content">
            <h1>🚀 {user.name}의 React 학습 여정</h1>
            <p>각 Step을 클릭해서 학습 내용을 확인해보세요!</p>
            <UserProfile />
          </div>
        );
    }
  };

  return (
    <div className={`App ${theme}`}>
      <nav className="step-navigation">
        <button 
          onClick={() => handleStepChange('home')}
          className={currentStep === 'home' ? 'active' : ''}
        >
          🏠 홈
        </button>
        <button 
          onClick={() => handleStepChange('step1-4')}
          className={currentStep === 'step1-4' ? 'active' : ''}
        >
          🏗️ Step 1-4: 채팅 UI
        </button>
        <button 
          onClick={() => handleStepChange('step5')}
          className={currentStep === 'step5' ? 'active' : ''}
        >
          📝 Step 5: 폼
        </button>
        <button 
          onClick={() => handleStepChange('stats')}
          className={currentStep === 'stats' ? 'active' : ''}
        >
          📊 통계
        </button>
        {/* 테마 토글 버튼 추가 */}
        <ThemeToggle />
      </nav>
      
      <main className="step-content">
        {renderStepContent()}
      </main>
    </div>
  );
};

// 메인 App 컴포넌트 (Provider로 감싸기)
function App() {
  return (
    <AppProvider>
      <AppContent />
    </AppProvider>
  );
}

export default App;