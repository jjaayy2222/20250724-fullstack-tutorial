// frontend/chatbot-app/src/App.js
import React from 'react';
import './App.css';
import StressReliefForm from './StressRelirefForm';

/* step_1 ~ 4
function App() {
  return (
    <div className="app">
      <h1>Chat App</h1>
      <div className="chat-box">
        <div className="messages-list">
          <div className="user-message">Hello</div>
          <div className="ai-message">Your message is: "Hello"</div>
        </div>
        <form className="message-form">
          <input 
            type="text" 
            className="message-input" 
            placeholder="메시지를 입력하세요"
          />
          <button type="submit">Send</button>
        </form>
      </div>
    </div>
  );
} */

// step_5
  function App() {
  return (
    <div className="App">
      <h1>Jay의 Step 5 - 폼 다루기 🎯</h1>
      <StressReliefForm />
    </div>
  );
}

export default App;