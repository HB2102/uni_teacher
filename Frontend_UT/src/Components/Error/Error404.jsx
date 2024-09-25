import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
const Error404 = () => {
    const navigate = useNavigate();
    
    const handleBackHome = ()=> {
        navigate('/search', { replace: true });
      }
  

    return (
        <>
         <div className='flex flex-row gap-5 items-center justify-center flex-wrap mt-5'>       
                     <main className="farmer-motion h-50 w-full flex flex-col justify-center items-center">
                    <h1 className="pt-12 text-[140px] font-extrabold text-text-gray dark:text-white tracking-widest">404</h1>
                    <div className="bg-red-900 dark:text-text-gray text-white px-2 text-sm rounded rotate-12 absolute">
                        نتیجه‌ای یافت نشد
                    </div>
                    <button class="mt-0">
                      <a
                        className="relative inline-block text-sm font-medium dark:text-red-900 dark:active:text-red-500 text-red-500 group active:text-red-400 focus:outline-none focus:ring"
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
            {/* <main>
        <section class="py-12 relative w-full  flex justify-center items-center">
            <div class="mx-auto max-w-[85rem] px-4 sm:px-6 lg:px-8 relative">

                <div class=" w-full h-auto text-center mb-7">
                    <div class="w-full h-auto  px-7 py-8 rounded-2xl">
                        <h1 class="font-manrope font-black text-[200px] leading-relaxed text-indigo-600 text-center mb-6">
                            4<span class="text-indigo-200">0</span>4</h1>
                        <p class="font-medium text-2xl leading-9 text-gray-900 text-center mb-4">Looks like You've got
                            lost....</p>
                        <p class="font-medium text-lg leading-9 text-gray-600 text-center mb-6">The page you're looking for
                            dosen't exist or has been moved</p>
                        <button onClick={handleBackHome} class="w-44 bg-indigo-600 text-white rounded-full cursor-pointer font-semibold text-center shadow-xs transition-all duration-500 py-3.5 px-6 text-sm hover:bg-indigo-700">GO
                            HOME</button>
                    </div>
                </div>
            </div>
        </section>
    </main> */}
        </>
    );
};

export default Error404;
