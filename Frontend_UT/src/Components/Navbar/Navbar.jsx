import React, { useState } from 'react';
import "./Nav.css";
import { Bars3Icon, XMarkIcon } from "@heroicons/react/24/outline";
import { PiStudent } from "react-icons/pi";
import { FaUniversity } from "react-icons/fa";
import { LiaChalkboardTeacherSolid } from "react-icons/lia";
import { motion } from 'framer-motion'; 
import DarkModeSwitch from './dark';


function MenuBar() {
  const [isMenuOpen, setIsMenuOpen] = useState(false);

  const toggleMenu = () => {
    setIsMenuOpen(!isMenuOpen);
  };

  return (
    <motion.div 
    initial={{ y: -100, opacity: 0 }} 
    animate={{ y: 0, opacity: 1 }} 
    transition={{ duration: 1 }} 
  >
    <div >
      <div>
        <header className="navbar  flex justify-between items-center bg-teal-800 bg-opacity-25 w-full mt-6 mb-1 relative p-7 rounded-3xl">

         
          <div className="flex items-center">
          <FaUniversity className="bg-teal-500 text-teal-800 border border-teal-800  w-10 h-10 rounded-full mr-3"/>
            < LiaChalkboardTeacherSolid className="bg-teal-500  text-teal-800 border border-teal-800  w-10 h-10 rounded-full mr-3"/>
            
            < PiStudent className=" bg-teal-500  text-teal-800 border border-teal-800  w-8 h-8 rounded-full mr-3"/>
            {/* <span className="text-xl font-bold">فوکینگ لوگو</span> */}
          </div>

          
          <div className="sm:hidden">
            {isMenuOpen ? (
              <XMarkIcon onClick={toggleMenu} className="h-6 w-6 cursor-pointer" strokeWidth={2} />
            ) : (
              <Bars3Icon onClick={toggleMenu} className="h-6 w-6 cursor-pointer" strokeWidth={2} />
            )}
          </div>

          <DarkModeSwitch /> 
          <nav className={`sm:flex ${isMenuOpen ? 'block' : 'hidden'} absolute sm:relative top-full left-0 w-full sm:w-auto bg-gray-900 sm:bg-transparent p-6 sm:p-0 z-10`}>
            <ul className="flex flex-col gap-3 sm:flex-row sm:space-x-4 items-center">
              <li>
                <a href="#about" className="relative text-white hover:text-teal-400 transition-all duration-300 hover:underline after:content-[''] after:absolute after:block after:w-0 after:h-0.5 after:bg-teal-400 after:transition-all after:duration-300 after:left-1/2 after:bottom-0 hover:after:w-full hover:after:left-0">
                  درباره‌ی ما
                </a>
              </li>
              <li>
                <a href="#blog" className="relative text-white hover:text-teal-400 transition-all duration-300 hover:underline after:content-[''] after:absolute after:block after:w-0 after:h-0.5 after:bg-teal-400 after:transition-all after:duration-300 after:left-1/2 after:bottom-0 hover:after:w-full hover:after:left-0">
                  ارسال درخواست
                </a>
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
