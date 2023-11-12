import './App.css';
import {useState} from 'react'

function App() {
  const [counter, setCounter] = useState(0);
  return (
    <div className="App">
      <button onClick = {() => setCounter( (prevClick) => prevClick + 1 )}>up</button>
      <h1>{counter}</h1>
      <button onClick = {() => setCounter( (prevClick) => prevClick - 1 )}>down</button>
    </div>
  );
}

export default App;
