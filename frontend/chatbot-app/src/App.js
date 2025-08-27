// frontend/chatbot-app/src/App.js

import React, { useEffect } from 'react';
import './App.css';
import { useAppContext } from './contexts/AppContext';
import { Routes, Route } from "react-router-dom";
import Step1to4 from "./components/Step1to4";               // 기존 컴포넌트 import
import Step5 from "./components/Step5";
import Dashboard from "./components/Dashboard";             // Step6 대시보드

const App = () => {
  const { theme } = useAppContext();

  useEffect(() => {
    console.log('테마 적용 중:', theme);
  }, [theme]);

  return (
    <div className={`App ${theme}`}>
      <Routes>
        <Route path="/" element={<Step1to4 />} />  {/* Step1-4 페이지*/}
        <Route path="/form" element={<Step5 />} />  {/* Step5 폼 */}|
        <Route path="/dashboard" element={<Dashboard />} />  {/* Step6 대시보드 */}
      </Routes>
    </div>
  );
};

export default App;
