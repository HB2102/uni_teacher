import React, { useState, useEffect } from 'react';
import { IoMdArrowDropdown } from "react-icons/io";
import TeacherRate from './TeacherRate';
const TeacherProfile = () => {
  
 return(
  <section  className="relative pt-40 pb-24 bg-white ">
  <img
    src="https://pagedone.io/asset/uploads/1705473908.png"
    alt="cover"
    className="w-full absolute top-0 left-0 z-0 h-60 object-cover"
  />
  <div className="w-full max-w-7xl mx-auto px-6 md:px-8">
    <div className="flex items-center justify-center sm:justify-start relative z-10 mb-5">
      <img
        src="https://pagedone.io/asset/uploads/1705471668.png"
        alt="user avatar"
        className="border-4 border-white rounded-full object-cover"
      />
    </div>
    <div className="flex items-center justify-center flex-col sm:flex-row sm:justify-between mb-5 space-y-5 sm:space-y-0 sm:space-x-5">
      <div>
        <h3 className=" font-manrope font-bold text-4xl text-gray-900 text-center sm:text-left">اسم استاد </h3>
        <p className="pt-3 font-normal text-base leading-7 text-gray-500 text-center sm:text-left">
          {/* Engineer at BB Agency Industry <br className="hidden sm:block" />
          New York, United States */}
        </p>
      </div>
      <button className="py-3.5 px-5 flex rounded-full bg-indigo-600 items-center shadow-sm transition-all duration-500 hover:bg-indigo-700">
        <svg
          width="20"
          height="20"
          viewBox="0 0 20 20"
          fill="none"
          xmlns="http://www.w3.org/2000/svg"
        >
          <path
            d="M11.3011 8.69881L8.17808 11.8219M8.62402 12.5906L8.79264 12.8819C10.3882 15.6378 11.1859 17.0157 12.2575 16.9066C13.3291 16.7974 13.8326 15.2869 14.8397 12.2658L16.2842 7.93214C17.2041 5.17249 17.6641 3.79266 16.9357 3.0643C16.2073 2.33594 14.8275 2.79588 12.0679 3.71577L7.73416 5.16033C4.71311 6.16735 3.20259 6.67086 3.09342 7.74246C2.98425 8.81406 4.36221 9.61183 7.11813 11.2074L7.40938 11.376C7.79182 11.5974 7.98303 11.7081 8.13747 11.8625C8.29191 12.017 8.40261 12.2082 8.62402 12.5906Z"
            stroke="white"
            strokeWidth="1.6"
            strokeLinecap="round"
          />
        </svg>
        <span className="px-2 font-semibold text-base leading-7 text-white">Send Message</span>
      </button>
    </div>
    
    <TeacherRate/>

    <div className="flex flex-wrap justify-center sm:justify-start items-center gap-4">
      <a
        href="#"
        className="rounded-full py-3 px-6 bg-stone-100 text-gray-700 font-semibold text-sm leading-6 transition-all duration-500 hover:bg-stone-200 hover:text-gray-900"
      >
        Ux Research
      </a>
      <a
        href="#"
        className="rounded-full py-3 px-6 bg-stone-100 text-gray-700 font-semibold text-sm leading-6 transition-all duration-500 hover:bg-stone-200 hover:text-gray-900"
      >
        CX Strategy
      </a>
      <a
        href="#"
        className="rounded-full py-3 px-6 bg-stone-100 text-gray-700 font-semibold text-sm leading-6 transition-all duration-500 hover:bg-stone-200 hover:text-gray-900"
      >
        Project Manager
      </a>
    </div>
  </div>

</section>
                                      
 )
};

export default TeacherProfile;
