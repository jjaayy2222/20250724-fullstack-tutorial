import logo from './logo.svg';
import './App.css';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          <strong style={{ fontSize: '25px', color: 'lightpink' }}>
            🎉 안녕하세요! 😊</strong><br />
          <strong style={{ fontSize: '40px', color: 'lightyellow' }}>
            ✨ Welcome to Jay's first React app! 🚀
          </strong>

          {/* 
          // 만약 두 개의 별개 단락으로 만들고 싶다면 (하지만 이 경우엔 <br />이 더 흔함)
            <p>🎉 안녕하세요! 😊</p>
            <p>✨ Welcome to Jay's first React app! 🚀</p>
          */}
          
          { // 원래 코드
          /*Edit <code>src/App.js</code> and save to reload.*/
          }
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React          
        </a>
      </header>
    </div>
  );
}

export default App;
