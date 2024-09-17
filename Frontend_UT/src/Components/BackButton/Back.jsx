import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
const Back = () => {
    const navigate = useNavigate();
    
    const handleBackHome = ()=> {
        navigate('/', { replace: true });
      }
  

    return (
        <>
        
         <div onClick={handleBackHome} dir='rtl' className="w-full flex h-full items-end lg:w-4/5 lg:mr-auto text-base md:text-sm text-gray-600 px-4 pt-5 mb-3 mx-7">
                <span className="text-base text-teal-600 font-bold">&lt;</span>{' '}
                <a className="text-base md:text-sm text-teal-600 font-bold no-underline hover:underline">
                    بازگشت به صفحه‌ی اصلی
                </a>
            </div>
           
        </>
    );
};

export default Back;
