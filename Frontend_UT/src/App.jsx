import { useState } from 'react'
import React from 'react';
import '../tailwind.config.js'
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import './App.css'
import SignIn from './Components/SignIn/SignIn';
import MenuBar from './Components/Navbar/Navbar';
import Main from './Components/Main/Main.jsx';
import LandingPage from './Components/Landing-page/LandingPage.jsx';
import DarkModeSwitch from './Components/Navbar/dark.jsx';


function App() {
  return (
    <Router>
    <div>
      <Routes>
        <Route path="/" element={<SignIn />} />
        <Route path="/home" element={<LandingPage />} />
        <Route path="/dark" element={<DarkModeSwitch />} />
       
      </Routes>
    </div>
  </Router>
  )
}

export default App
