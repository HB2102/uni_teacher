import { useState } from 'react'
import React from 'react';
import '../tailwind.config.js'
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import './App.css'
import LandingPage from './Components/Landing-page/LandingPage.jsx';
import Searchbar from './Components/SearchBar/search page/Searchbar.jsx';
import UserPanel from './Components/User/UserPanel.jsx';
import Request from './Components/Request/Request.jsx';
import AboutUs from './Components/About/AboutUs.jsx';
import UserInfo from './Components/User/UserInfo.jsx';
import SearchPage from './Components/SearchBar/search page/SearchPage.jsx';
import SubjectTeachers from './Components/Relations/Sub-Teacher/SubjectTeachers.jsx';
import Show from './Components/show.jsx';
import TeacherProfile from './Components/Teacher/TeacherProfile.jsx';
import Skeleton from 'react-loading-skeleton';
import 'react-loading-skeleton/dist/skeleton.css';
import SkeletonReviewCard from './Components/Skeletion/CardSkeletion.jsx';
import UniCardSkeleton from './Components/Skeletion/unicardSkeleton.jsx';
import CardSkeleton from './Components/Skeletion/MainSkeleton.jsx';
import NavbarSkeleton from './Components/Skeletion/NavbarSkeleton.jsx';


function App() {
  return (
    <Router>
    <div >
      <Routes>
        <Route path="/" element={<LandingPage />} />
        <Route path="/user-panel" element={< UserPanel/>} />
        <Route path="/request" element={<Request />} />
        <Route path="/AboutUs" element={<AboutUs />} />
        <Route path='/search' element={<SearchPage/>} />
        <Route path='/user-info' element={<UserInfo/>} />
        <Route path='/subject-teachers' element={<SubjectTeachers/>} />
        <Route path='/teacher-profile' element={<TeacherProfile/>} />
        <Route path="/test" element={<NavbarSkeleton />} />
      </Routes>
    </div>
  </Router>
  )
}

export default App
