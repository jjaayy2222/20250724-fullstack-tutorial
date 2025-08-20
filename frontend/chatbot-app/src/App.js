// frontend/chatbot-app/src/App.js
import React from 'react';
import './App.css';

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
}

export default App;