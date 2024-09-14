import './App.css';
import Navbar from './Navbar';
import MainBody from './MainBody';

function App() {
  return (
    <div>
      <Navbar>
      </Navbar>
      <div className="row" style={{ gap: "10px" }}></div>
      <MainBody />
      
    </div>
  );
}

export default App;
