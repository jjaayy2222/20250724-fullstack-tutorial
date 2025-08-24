// frontend/chatbot-app/src/components/UserProfile.js

import React from 'react';
import { useAppContext } from '../contexts/AppContext';
import './UserProfile.css';

const UserProfile = () => {
    // 전역 상태에서 사용자 정보 가져오기
    const { user, updateUser } = useAppContext();

    // 사용자 이름 변경 함수
    const handleNameChange = () => {
        const newName = prompt('새로운 이름을 입력하세요:', user.name);
        if (newName) {
            updateUser({ name: newName }); // 전역 상태 업데이트
        }
    };

    return (
        <div className="user-profile">
            <div className="profile-info">
                <h3>👤 사용자 프로필</h3>
                <p><strong>이름:</strong> {user.name}</p>
                <p><strong>이메일:</strong> {user.email}</p>
            </div>
            <button onClick={handleNameChange} className="edit-button">
            ✏️ 이름 변경
            </button>
        </div>
    );
};

export default UserProfile;