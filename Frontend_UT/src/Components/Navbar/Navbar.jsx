import React, { useState } from 'react';
import "./Nav.css";
import { Bars3Icon, XMarkIcon } from "@heroicons/react/24/outline";
import { PiStudent } from "react-icons/pi";
import { FaUniversity } from "react-icons/fa";
import { LiaChalkboardTeacherSolid } from "react-icons/lia";

function MenuBar() {
  const [isMenuOpen, setIsMenuOpen] = useState(false);

  const toggleMenu = () => {
    setIsMenuOpen(!isMenuOpen);
  };

  return (
    <div className="min-h-screen bg-gray-900 text-white flex flex-col items-center justify-center p-4">
      <div style={{ minHeight: 'calc(100vh - 60px)' }}>
        <header className="navbar flex justify-between items-center bg-teal-800 bg-opacity-25 w-full max-w-5xl mb-6 relative p-7 rounded-3xl">
          {/* Logo */}
          <div className="flex items-center">
            <div className="bg-teal-500 w-8 h-8 rounded-full mr-3"></div>
            <span className="text-xl font-bold">فوکینگ لوگو</span>
          </div>

          {/* Menu Toggle Button */}
          <div className="sm:hidden">
            {isMenuOpen ? (
              <XMarkIcon onClick={toggleMenu} className="h-6 w-6 cursor-pointer" strokeWidth={2} />
            ) : (
              <Bars3Icon onClick={toggleMenu} className="h-6 w-6 cursor-pointer" strokeWidth={2} />
            )}
          </div>

          {/* Navigation Menu */}
          <nav className={`sm:flex ${isMenuOpen ? 'block' : 'hidden'} absolute sm:relative top-full left-0 w-full sm:w-auto bg-gray-900 sm:bg-transparent p-6 sm:p-0 z-10`}>
            <ul className="flex flex-col gap-3 sm:flex-row sm:space-x-4 items-center">
              <li>
                <a href="#about" className="relative text-white hover:text-teal-400 transition-all duration-300 hover:underline after:content-[''] after:absolute after:block after:w-0 after:h-0.5 after:bg-teal-400 after:transition-all after:duration-300 after:left-1/2 after:bottom-0 hover:after:w-full hover:after:left-0">
                  About
                </a>
              </li>
              <li>
                <a href="#blog" className="relative text-white hover:text-teal-400 transition-all duration-300 hover:underline after:content-[''] after:absolute after:block after:w-0 after:h-0.5 after:bg-teal-400 after:transition-all after:duration-300 after:left-1/2 after:bottom-0 hover:after:w-full hover:after:left-0">
                  Blog
                </a>
              </li>
              <li>
                <a href="#testimonials" className="relative text-white hover:text-teal-400 transition-all duration-300 hover:underline after:content-[''] after:absolute after:block after:w-0 after:h-0.5 after:bg-teal-400 after:transition-all after:duration-300 after:left-1/2 after:bottom-0 hover:after:w-full hover:after:left-0">
                  Testimonials
                </a>
              </li>
              <li>
                <a href="#resources" className="relative text-white hover:text-teal-400 transition-all duration-300 hover:underline after:content-[''] after:absolute after:block after:w-0 after:h-0.5 after:bg-teal-400 after:transition-all after:duration-300 after:left-1/2 after:bottom-0 hover:after:w-full hover:after:left-0">
                  Resources
                </a>
              </li>
            </ul>
          </nav>
        </header>

        <main className="flex flex-col-reverse gap-9 lg:flex-row items-center w-full max-w-5xl mt-6 sm:py-5 md:py-22 lg:py-32 xl:py-32">
          <div className="flex flex-col items-start lg:w-1/2 p-4 text-center lg:text-left">
            <h1 className="text-4xl md:text-5xl lg:text-6xl font-bold mb-6 rtl">توضیحات متفرقه در تایتل این مجموعه</h1>
            <p className="mb-6">یادآوری: یکم فونت زشته و فاصله‌ی بین خطوط باید اصلاح بشه </p>
            <div className="flex w-full mb-4 flex-col sm:flex-row">
              <input
                type="text"
                placeholder="Search..."
                className="flex-grow p-3 rounded-full text-black mb-3 sm:mb-0 sm:mr-2"
              />
              <button className="bg-teal-500 px-6 py-3 rounded-full text-white hover:bg-teal-600">Search</button>
            </div>
            <ul className="space-y-2 text-sm text-left">
              <li className="flex items-center">
                <span className="bg-teal-500 rounded-full w-2 h-2 mr-2"></span>
                صفحه باید راست چین بشه
              </li>
              <li className="flex items-center">
                <span className="bg-teal-500 rounded-full w-2 h-2 mr-2"></span>
                خود نوشته ها راست چین نشدن
              </li>
              <li className="flex items-center">
                <span className="bg-teal-500 rounded-full w-2 h-2 mr-2"></span>
                در قسمت بعدی لاگین و قرار میدی
              </li>
              <li className="flex items-center">
                <span className="bg-teal-500 rounded-full w-2 h-2 mr-2"></span>
                دست نزن به فرانت بکند کار کثیف
              </li>
            </ul>
          </div>
          <div className="lg:w-1/2 ">
            <div className="w-full rounded-lg overflow-hidden relative">
                <FaUniversity style={{ fontSize: '450px', opacity: '0.15' }} className="w-full object-cover text-teal-500" />

                <PiStudent 
                style={{ 
                    fontSize: '250px', 
                    position: 'absolute', 
                    bottom: '10px',
                    right: '30px' 
                }} 
                className="text-teal-800" 
                />
                
                {/* <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ5YYQiChP4lAhGjF-1EjyII_YQnJvCizikRA&s" alt="Placeholder" className="w-full object-cover" /> */}
            </div>
          </div>
        </main>

        <div className="lg:w-1/2 pb-4 ">
            <div className="w-full rounded-lg  overflow-hidden relative">
                <LiaChalkboardTeacherSolid style={{ fontSize: '450px', opacity: '0.15' }} className="w-full object-cover text-teal-500" />

                <FaUniversity 
                style={{ 
                    fontSize: '250px', 
                    position: 'absolute', 
                    bottom: '10px',
                    right: '30px'
                }} 
                className="text-teal-800" 
                />
                
                {/* <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ5YYQiChP4lAhGjF-1EjyII_YQnJvCizikRA&s" alt="Placeholder" className="w-full object-cover" /> */}
            </div>
          </div>
      </div>
    </div>
  );
}

export default MenuBar;
