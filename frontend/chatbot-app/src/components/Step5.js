// frontend/chatbot-app/src/components/Step5.js


import React, { useState } from 'react';
import './Step1to4.css';

function Step1to4() {
    const [count, setCount] = useState(0);
    const [todos, setTodos] = useState([]);
    const [todoInput, setTodoInput] = useState('');

    const addTodo = () => {
        if (todoInput.trim()) {
            setTodos([...todos, { id: Date.now(), text: todoInput, completed: false }]);
            setTodoInput('');
        }
    };

    const toggleTodo = (id) => {
        setTodos(todos.map(todo => 
            todo.id === id ? { ...todo, completed: !todo.completed } : todo
        ));
    };

    const deleteTodo = (id) => {
        setTodos(todos.filter(todo => todo.id !== id));
    };

    return (
        <div className="step1to4-container">
            <h2>🏗️ Step 1-4: React 기초 완성</h2>
    
            {/* 카운터 섹션 */}
            <div className="counter-section">
                <h3>카운터: {count}</h3>
                <button onClick={() => setCount(count + 1)}>+1</button>
                <button onClick={() => setCount(count - 1)}>-1</button>
                <button onClick={() => setCount(0)}>리셋</button>
            </div>

            {/* 할일 목록 섹션 */}
            <div className="todo-section">
                <h3>할일 목록</h3>
                <div className="todo-input">
                    <input
                    type="text"
                    value={todoInput}
                    onChange={(e) => setTodoInput(e.target.value)}
                    placeholder="할일을 입력하세요..."
                    onKeyPress={(e) => e.key === 'Enter' && addTodo()}
                    />
                <button onClick={addTodo}>추가</button>
            </div>
            <ul className="todo-list">
                {todos.map(todo => (
                    <li key={todo.id} className={todo.completed ? 'completed' : ''}>
                    <span onClick={() => toggleTodo(todo.id)}>{todo.text}</span>
                    <button onClick={() => deleteTodo(todo.id)}>삭제</button>
                    </li>
                ))}
            </ul>
        </div>
    </div>
    );
}

export default Step1to4;