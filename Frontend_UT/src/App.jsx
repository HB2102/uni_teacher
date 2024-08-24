import { useState } from 'react'
import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import './App.css'
import SignIn from './Components/SignIn/SignIn';

function App() {
  return (
    <Router>
    <div>
      <Routes>
        <Route path="/" element={<SignIn />} />
      </Routes>
    </div>
  </Router>
  )
}

export default App
