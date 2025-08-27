// frontend/chatbot-app/src/index.js

import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';  // AppContent가 export된 파일
import { AppProvider } from './contexts/AppContext';
import { BrowserRouter } from 'react-router-dom';

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <AppProvider>       {/* App Context 제공 */}
      <BrowserRouter>   {/* Router 안에 App */}
        <App />
      </BrowserRouter>
    </AppProvider>
  </React.StrictMode>
);
