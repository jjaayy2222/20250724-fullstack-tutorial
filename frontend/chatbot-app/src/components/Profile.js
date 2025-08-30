// src/components/Profile.js
import React from 'react';
import UserProfile from './UserProfile';
import ThemeToggle from './ThemeToggle';

const Profile = () => (
  <div className="profile-container">
    <h2>👤 Profile Settings</h2>
    <div className="profile-content">
      <div className="theme-section">
        <h3>🎨 Theme Preferences</h3>
        <ThemeToggle />
      </div>
      <div className="user-section">
        <h3>👤 User Information</h3>
        <UserProfile />
      </div>
    </div>
  </div>
);

export default Profile;
