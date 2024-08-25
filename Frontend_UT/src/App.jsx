import { useState } from 'react'
import React from 'react';
import '../tailwind.config.js'
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import './App.css'
import Signin from './Components/SignIn/SignIn';
import MenuBar from './Components/Navbar/Navbar';
import Main from './Components/Main/Main.jsx';
import LandingPage from './Components/Landing-page/LandingPage.jsx';
import DarkModeSwitch from './Components/Navbar/dark.jsx';


function App() {
  return (
    <Router>
    <div>
      <Routes>
        <Route path="/" element={<Signin />} />
        <Route path="/home" element={<LandingPage />} />

       
      </Routes>
    </div>
  </Router>
  )
}

export default App
