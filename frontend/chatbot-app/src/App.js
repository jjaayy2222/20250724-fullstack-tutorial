// frontend/chatbot-app/src/App.js

import React, { useEffect } from 'react';
import './App.css';
import { useAppContext } from './contexts/AppContext';
import { Routes, Route } from 'react-router-dom';

// 모든 컴포넌트 import
import NavBar from './components/NavBar';
import Home from './components/Home';
import Stats from './components/Stats';
import Dashboard from './components/Dashboard';
import Profile from './components/Profile';
import Practice from './components/Practice';
import Settings from './components/Settings';


const App = () => {
  const { theme } = useAppContext();

  useEffect(() => {
    console.log('테마 적용 중:', theme);
  }, [theme]);

  return (
    <div className={`App ${theme}`}>
      <NavBar />
      
      <main className="main-content">
        <Routes>
          {/* 추가 개선  <Route path="/" element={<Welcome />} />*/}
          <Route path="/home" element={<Home />} />
          <Route path="/stats" element={<Stats />} />
          <Route path="/dashboard" element={<Dashboard />} />
          <Route path="/profile" element={<Profile />} />
          <Route path="/practice" element={<Practice />} />
          <Route path="/settings" element={<Settings />} />  {/* <- 새로 추가 */}
        </Routes>
      </main>
    </div>
  );
};

export default App;