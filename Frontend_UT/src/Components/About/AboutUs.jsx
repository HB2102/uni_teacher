import React from 'react';
import { FaFacebook, FaTwitter, FaInstagram, FaLinkedin } from 'react-icons/fa';
import { FaGithub } from 'react-icons/fa';
import {BiLogoGmail , BiLogoTelegram } from "react-icons/bi";
import { useNavigate } from 'react-router-dom';
const AboutUs = () => {
    const navigate = useNavigate();
    const handleBackHome = ()=> {
        navigate("/");
      }
  return (
    <div className="flex items-center justify-center min-h-screen bg-gray-100" dir='rtl'>
      <div className="sm:flex flex-col items-center max-w-screen-xl bg-white p-10 shadow-lg rounded-lg">

       
        <div className=" flex sm:w-3/5 p-10">
          <div className="image object-center text-center">
            <img src="https://iworkedon.com/images/hero.svg" alt="Company" />
          </div>
          
        </div>

    
      

        <div className="sm:w-1/2 p-5">
          <div className="text ">
            <span className="text-gray-500 border-b-2 border-indigo-600 uppercase">درباره‌ی ما</span>
            <h2 className="my-4 font-bold text-3xl sm:text-4xl">
              درباره‌ی <span className="text-indigo-600">اهداف ما</span>
            </h2>
            <p className="text-gray-700 text-lg">
             شرکت ما خیلی خوبه ما خیلی خوبیم و سعی داریم تا امکانات رفاهی فراهم کنیم تا دانسجوها بتونن راحت انتخاب واحد کنن و استادای آشغالی نره تو پاچشون
            </p>
            <div className="flex justify-center space-x-4 mt-6" dir='ltr'>
              <BiLogoTelegram className="opacity-90 transition-opacity hover:opacity-100 text-indigo-600 w-9 h-9 cursor-pointer" />
              <FaGithub className="opacity-90 transition-opacity hover:opacity-100 text-indigo-600 w-9 h-9 cursor-pointer" />
              <BiLogoGmail className="opacity-90 transition-opacity hover:opacity-100 text-indigo-600 w-9 h-9 cursor-pointer" />
              <FaLinkedin className="opacity-90 transition-opacity hover:opacity-100 text-indigo-600 w-9 h-9 cursor-pointer" />
            </div>
          </div>
        </div>
        <div className='py-3' onClick={handleBackHome} > 
                    <span className="text-base text-indigo-600 font-bold">&lt;</span>{' '}
                    <a  className="text-base md:text-sm text-indigo-600 font-bold no-underline hover:underline">
                        بازگشت به صفحه‌ی اصلی
                    </a>
        </div>
      </div>

    </div>
  );
};

export default AboutUs;
