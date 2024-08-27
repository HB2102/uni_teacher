import { useState } from 'react'
import React from 'react';
import '../tailwind.config.js'
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import './App.css'
import LandingPage from './Components/Landing-page/LandingPage.jsx';
import Searchbar from './Components/SearchBar/Searchbar.jsx';
import FooterWithSocialLinks from './Components/show.jsx';



function App() {
  return (
    <Router>
    <div>
      <Routes>
        
        <Route path="/" element={<LandingPage />} />
        <Route path="/test" element={<FooterWithSocialLinks />} />
       
      </Routes>
    </div>
  </Router>
  )
}

export default App
