import { useState } from 'react'
import React from 'react';
import '../tailwind.config.js'
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import './App.css'
import SignIn from './Components/SignIn/SignIn';
import MenuBar from './Components/Navbar/Navbar';

function App() {
  return (
    <Router>
    <div>
      <Routes>
        <Route path="/" element={<SignIn />} />
        <Route path="/home" element={<MenuBar />} />
      </Routes>
    </div>
  </Router>
  )
}

export default App
