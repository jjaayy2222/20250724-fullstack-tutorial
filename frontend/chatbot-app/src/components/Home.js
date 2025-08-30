// /frontend/chatbot-app/src/components/Home.js

import React from "react";
import { Link } from "react-router-dom";  // Link 컴포넌트 import
import "./Home.css";

const Home = () => (
  <div className="home-container">
    <header className="hero-section">
      <h1>🤖 Jay's Chatbot Application 🤖</h1>
      <p>Welcome to the enhanced React chatbot experience!</p>
    </header>
    
    <section className="features-preview">
      <h2>Available Features</h2>
      <div className="feature-grid">
        <div className="feature-card">
          <h3>📊 Statistics</h3>
          <p>View your usage statistics and progress</p>
          {/* Link를 사용해 Statistics 페이지로 이동 */}
          <Link to="/stats" className="feature-link">Go to Stats</Link>
        </div>
        
        <div className="feature-card">
          <h3>🎛️ Dashboard</h3>
          <p>Control panel for managing settings</p>
          {/* Link를 사용해 Dashboard 페이지로 이동 */}
          <Link to="/dashboard" className="feature-link">Go to Dashboard</Link>
        </div>
        
        <div className="feature-card">
          <h3>👤 Profile</h3>
          <p>Manage your profile and preferences</p>
          {/* Link를 사용해 Profile 페이지로 이동 */}
          <Link to="/profile" className="feature-link">Go to Profile</Link>
        </div>
        
        <div className="feature-card">
          <h3>🧪 Practice</h3>
          <p>Development and testing area</p>
          {/* Link를 사용해 Practice 페이지로 이동 */}
          <Link to="/practice" className="feature-link">Go to Practice</Link>
        </div>

        <div className="feature-card">
          <h3>⚙️ Settings</h3>
          <p>Manage application settings</p>
          {/* Link를 사용해 Practice 페이지로 이동 */}
          <Link to="/settings" className="feature-link">Go to Settings</Link>
        </div>


      </div>
    </section>
  </div>
);

export default Home;
