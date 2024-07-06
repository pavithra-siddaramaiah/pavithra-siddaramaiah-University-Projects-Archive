import React from 'react';
import "./App.css";
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';

import NavBar from './components/NavBar/NavBar';
import About from './components/About/About';
import Projects from './components/Projects/Projects';
import Home from './components/Home/Home';
import Skills from './components/Skills/Skills';
import Contact from './components/Contact/Contact';
import GoHome from './components/GoHome/GoHome';

const App = () => {
  return (
      <Router>
          <div>
              <NavBar />
              <Routes>
                  <Route path="/" element={<Home />} />
                  <Route path="/about" element={<About />} />
                  <Route path="/projects" element={<Projects />} />
                  <Route path="/skills" element={<Skills />} />
                  <Route path="/contact" element={<Contact />} />
              </Routes>
          </div>
      </Router>
  );
};
export default App;
