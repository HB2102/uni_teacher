
import React, { useState } from 'react'
import MenuBar from '../Navbar/Navbar'
import Main from '../Main/Main'
import SignIn from '../SignIn/SignIn'
const LandingPage = () => {

  

  return (
    <div className=" min-h-screen bg-gray-900 text-white flex flex-col  items-center justify-center p-4">
      <div style={{ minHeight: 'calc(100vh - 60px)' }}>
 <MenuBar>

 </MenuBar>
 <Main></Main>

 </div>
 </div>
  )
}

export default LandingPage

