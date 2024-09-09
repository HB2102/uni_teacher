import { useState } from 'react'
import React from 'react';
import '../tailwind.config.js'
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import './App.css'
import LandingPage from './Components/Landing-page/LandingPage.jsx';
import Searchbar from './Components/SearchBar/Searchbar.jsx';
import UserPanel from './Components/User/UserPanel.jsx';
import Request from './Components/Request/Request.jsx';

import AboutUs from './Components/About/AboutUs.jsx';
import OTPVerification from './Components/SignIn/verify.jsx';



function App() {
  return (
    <Router>
    <div >
      <Routes>
        <Route path="/" element={<LandingPage />} />
        <Route path="/user-panel" element={< UserPanel/>} />
        <Route path="/request" element={<Request />} />
        <Route path="/AboutUs" element={<AboutUs />} />
        <Route path='/test' element={<OTPVerification/>} />
      </Routes>
    </div>
  </Router>
  )
}

export default App
