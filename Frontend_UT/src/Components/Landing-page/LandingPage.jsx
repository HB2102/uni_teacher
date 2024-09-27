
import React, { useState,useEffect } from 'react'
import Cookies from 'js-cookie';
import MenuBar from '../Navbar/Navbar'
import Main from '../Main/Main'
import Footer from '../Footer/Footer'
const LandingPage = () => {

  const [isAuthenticated, setIsAuthenticated] = useState(false);

 
    useEffect(() => {
        const token = Cookies.get('auth_token');
        setIsAuthenticated(token !== undefined);
    }, []);

    const handleLogOut = () => {
        Cookies.remove('auth_token');
        setIsAuthenticated(false);
    };
    const handleLogin = () => {
      // Cookies.set('auth_token', 'your-token'); 
      setIsAuthenticated(true);
  };

  return (
  
    <div  className="overflow-x min-h-screen text-white flex flex-col  items-center justify-center p-4 ">
      <div >
 <MenuBar isAuthenticated={isAuthenticated} >

 </MenuBar>
 <Main isAuthenticated={isAuthenticated} 
              onLogOut={handleLogOut} 
              onLogin={handleLogin} ></Main>
  <Footer/>
 </div>
 </div>
  )
}

export default LandingPage

