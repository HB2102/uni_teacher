
import React, { useState } from 'react'
import MenuBar from '../Navbar/Navbar'
import Main from '../Main/Main'
import Footer from '../Footer/Footer'
const LandingPage = () => {

  

  return (
    <div className="overflow-x min-h-screen bg-gray-950 text-white flex flex-col  items-center justify-center p-4 ">
      <div >
 <MenuBar>

 </MenuBar>
 <Main></Main>
  <Footer/>
 </div>
 </div>
  )
}

export default LandingPage

