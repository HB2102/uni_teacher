import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
const Error404 = () => {
    const navigate = useNavigate();
    
    const handleBackHome = ()=> {
        navigate('/search', { replace: true });
      }
  

    return (
        <>
         <div className='flex flex-row gap-5 items-center justify-center flex-wrap mt-20'>       
                     <main className="farmer-motion h-80 w-full flex flex-col justify-center items-center">
                    <h1 className="text-9xl font-extrabold text-white tracking-widest">404</h1>
                    <div className="bg-red-900 px-2 text-sm rounded rotate-12 absolute">
                        نتیجه‌ای یافت نشد
                    </div>
                    <button class="mt-5">
                      <a
                        className="relative inline-block text-sm font-medium text-red-900 group active:text-red-500 focus:outline-none focus:ring"
                      >
                        <span
                          className="absolute inset-0 transition-transform translate-x-0.5 translate-y-0.5 bg-red-900 group-hover:translate-y-0 group-hover:translate-x-0"
                        ></span>
                
                        <span className="relative block px-8 py-3 bg-[#1A2238] border border-current">
                          <button onClick={handleBackHome}>بازگشت به صفحه‌ی جستجو</button>
                        </span>
                      </a>
                    </button>
                </main>

            </div>
        </>
    );
};

export default Error404;
