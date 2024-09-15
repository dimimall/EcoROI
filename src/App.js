import './App.css';
import Navbar from './Navbar';
import MainBody from './MainBody';
import HomePage from './HomePage';
import Projects from './Projects';


function App() {
  return (
    <div>
      <Navbar>
      </Navbar>
      <div className="row" style={{ gap: "10px" }}></div>
      <HomePage />
      
    </div>
  );
}

export default App;
