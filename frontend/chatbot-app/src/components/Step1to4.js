// frontend/chatbot-app/src/components/Step1to4.js

function Step1to4() {
    return (
        <div className="step1to4-container">
            <h2>🏗️ Step 1-4: 채팅 UI 기초</h2>
    
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

export default Step1to4;