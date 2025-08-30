// frontend/chatbot-app/src/components/NavBar.js

import React from "react";
import { NavLink } from "react-router-dom";
import "./NavBar.css";                                  // CSS 파일 import

const NavBar = () => (
    <nav className={"nav-bar"}>                             {/* 테마 클래스 적용 */}
        <NavLink to="/">🌱 basic</NavLink>                   {/* 기본 페이지 */}
        <NavLink to="/home">🏠 Home</NavLink>               {/* 랜딩 페이지 */}
        <NavLink to="/stats">📊 Stats</NavLink>             {/* Step1to4 */}
        <NavLink to="/dashboard">🎛️ Dashboard</NavLink>     {/* 통계 보기 */}
        <NavLink to="/profile">👤 Profile</NavLink>         {/* 프로필 관리 */}
        <NavLink to="/practice">🧪 Practice</NavLink>       {/* 제어판 */}
        <NavLink to="/settings">⚙️ Settings</NavLink>        {/* 새로 추가 */}
    </nav>
);

export default NavBar;
