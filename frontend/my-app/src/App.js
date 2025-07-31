import logo from './logo.svg';
import './App.css';

// components 실행 관련 임포트
import Counter from './components/Counter';
import CounterParent from './components/CounterParent';
import InputExample from './components/InputExample';


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

      {/* components 실습 관련을 b */}    
      {/* 👇 header 바깥 영역에 다른 컴포넌트들 추가 */}
      <main style={{ padding: '24px', background: '#fafaf7' }}>
        <Counter />
        <CounterParent />
        <InputExample />
      </main>


    </div>
  );
}

export default App;
