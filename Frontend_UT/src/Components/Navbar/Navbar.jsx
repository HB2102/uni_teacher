import React, { useState ,useEffect } from 'react';
import "./Nav.css";
import { Bars3Icon, XMarkIcon } from "@heroicons/react/24/outline";
import { PiStudent } from "react-icons/pi";
import { FaUniversity } from "react-icons/fa";
import { LiaChalkboardTeacherSolid } from "react-icons/lia";
import { motion } from 'framer-motion'; 
import DarkModeSwitch from './dark';
import { useNavigate } from 'react-router-dom';
import Cookies from 'js-cookie';


function MenuBar({ isAuthenticated }) {

 
  const navigate = useNavigate();
  const [isMenuOpen, setIsMenuOpen] = useState(false);
 

  const toggleMenu = () => setIsMenuOpen(!isMenuOpen);
  const handleAboutUs=()=>{
    navigate("/AboutUs")
  }
  const handleSendRequest=() =>{
    navigate("/request");
  }
 
  return (
    <motion.div 
    initial={{ y: -100, opacity: 0 }} 
    animate={{ y: 0, opacity: 1 }} 
    transition={{ duration: 1 }} 
  >
    <div >
      <div>
        <header className="navbar  flex justify-between items-center bg-teal-800 bg-opacity-25 w-full mt-6 mb-1 relative p-6 rounded-3xl">
        <DarkModeSwitch /> 
         
          <div className="hidden  md:flex items-center">

            < LiaChalkboardTeacherSolid className="bg-teal-500  text-teal-800 border border-teal-800  w-10 h-10 rounded-full mr-3"/>
            <FaUniversity className="bg-teal-500 text-teal-800 border border-teal-800  w-10 h-10 rounded-full mr-3"/>
            
            < PiStudent className=" bg-teal-500  text-teal-800 border border-teal-800  w-10 h-10 rounded-full mr-3"/>
          
          </div>

          
          <div className="sm:hidden">
            {isMenuOpen ? (
              <XMarkIcon onClick={toggleMenu} className="h-6 w-6 cursor-pointer" strokeWidth={2} />
            ) : (
              <Bars3Icon onClick={toggleMenu} className="h-6 w-6 cursor-pointer" strokeWidth={2} />
            )}
          </div>

          
          <nav className={`sm:flex ${isMenuOpen ? 'block' : 'hidden'} ${isMenuOpen ? 'bg-teal-950 mt-3 rounded-lg' : ''}  absolute sm:relative top-full left-0 w-full sm:w-auto  sm:bg-transparent p-6 sm:p-0 z-10 `}>
            <ul className="flex flex-col gap-3 sm:flex-row sm:space-x-4 items-center ">
            <li>
                    {isAuthenticated ? (
                        <h2 className="text-lg relative text-white hover:text-teal-400 transition-all duration-300 after:content-[''] after:absolute after:block after:w-0 after:h-0.5 after:bg-teal-400 after:transition-all after:duration-300 after:left-1/2 after:bottom-0 hover:after:w-full hover:after:left-0">
                            خروج
                        </h2>
                    ) : (
                        <h2 className="text-lg relative text-white hover:text-teal-400 transition-all duration-300 after:content-[''] after:absolute after:block after:w-0 after:h-0.5 after:bg-teal-400 after:transition-all after:duration-300 after:left-1/2 after:bottom-0 hover:after:w-full hover:after:left-0">
                            ثبت‌نام / ورود
                        </h2>
                    )}
                </li>
              <li onClick={handleAboutUs}>
                <h2 href="#about" className="text-lg relative text-white hover:text-teal-400 transition-all duration-300 after:content-[''] after:absolute after:block after:w-0 after:h-0.5 after:bg-teal-400 after:transition-all after:duration-300 after:left-1/2 after:bottom-0 hover:after:w-full hover:after:left-0">
                  درباره‌ی ما
                </h2>
              </li>
              <li onClick={handleSendRequest}
              >
             
                <p  href="#blog" className="  text-lg relative text-white hover:text-teal-400 transition-all duration-300  after:content-[''] after:absolute after:block after:w-0 after:h-0.5 after:bg-teal-400 after:transition-all after:duration-300 after:left-1/2 after:bottom-0 hover:after:w-full hover:after:left-0">
                  ارسال درخواست
                  <div className='text-black'>
                  </div>
                </p>
              
              </li>
            </ul>
            
          </nav>
          
        </header>

      </div>
    </div>
    
    </motion.div>
  );
}

export default MenuBar;
