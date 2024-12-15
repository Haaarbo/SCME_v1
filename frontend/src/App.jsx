import React from 'react';
import { BrowserRouter as Router, Route, Routes, Link } from 'react-router-dom';
import './App.css';
import Home from './paginas/Home';
import Cadastro from './paginas/Cadastro';
import Pesquisa from './paginas/Pesquisa';

function App() {
  return (
    <Router>
      <div className="App">
        <header>
          <h1>Central de Material Esterilizado</h1>
          <hr /> {/* Linha divisória */}
          <nav>
            <ul>
            <li><Link to="/">Home</Link></li>
            <li><Link to="/cadastro">Cadastro</Link></li>
            <li><Link to="/pesquisa">Pesquisa</Link></li>
            </ul>
          </nav>
        </header>
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/cadastro" element={<Cadastro />} />
            <Route path="/pesquisa" element={<Pesquisa />} />
          </Routes>
      </div>
    </Router>
  );
}


export default App;
