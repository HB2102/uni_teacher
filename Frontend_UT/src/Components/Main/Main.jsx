import React from 'react';
import { motion } from 'framer-motion';
import { PiStudent } from "react-icons/pi";
import { FaUniversity } from "react-icons/fa";
import { LiaChalkboardTeacherSolid } from "react-icons/lia";
import { useInView } from 'react-intersection-observer';
import { TfiEmail } from "react-icons/tfi";
import { MdOutlineAlternateEmail } from "react-icons/md";
import { useState } from 'react';
import Signin from '../SignIn/SignIn';
import MainSearchbar from '../SearchBar/MainSearchbar';
function Main() {
  const [showLogin, setShowLogin] = useState(false);


  const handleClickLogin = () => {
    setShowLogin(true);
  };

  const { ref: refFirstSection, inView: inViewFirstSection } = useInView({
    triggerOnce: true, 
    threshold: 0,
  });
  const { ref: refTheardSection, inView: inViewTheardSection } = useInView({
    triggerOnce: true, 
    threshold: 0, 
  });
 
  const { ref: refSecondSection, inView: inViewSecondSection } = useInView({
    triggerOnce: true,
    threshold: 0,
  });

  return (
    <div className="min-h-screen bg-gray-900 text-white flex flex-col items-center justify-center p-4">
      <div style={{ minHeight: 'calc(100vh - 60px)' }}>      
        <main className="flex flex-col gap-4 w-full max-w-6xl mt-6 sm:py-5 md:py-22 lg:py-22 xl:py-18">
          
          <motion.section 
            ref={refFirstSection}
            initial={{ x: 300, opacity: 0 }} 
            animate={inViewFirstSection ? { x: 0, opacity: 1 } : { x: 300, opacity: 0 }} 
            transition={{ duration: 1 }} 
            className="flex flex-col-reverse lg:flex-row items-center"
            dir="rtl"
          >
            <div className="lg:w-1/2">
              <div className="w-full rounded-lg overflow-hidden relative">
                <FaUniversity style={{ fontSize: '550px', opacity: '0.15' }} className="w-full object-cover text-gray-400" />
                <PiStudent
                  style={{
                    fontSize: '320px',
                    position: 'absolute',
                    bottom: '10px',
                    right: '30px'
                  }}
                  className="text-teal-800"
                />
              </div>
            </div>
            <div className="flex flex-col gap-2 items-start lg:w-1/2 p-4 text-center lg:text-right">
              <h1 className="text-4xl lg:leading-relaxed md:text-5xl lg:text-6xl font-bold mb-6">توضیحات متفرقه در تایتل این مجموعه</h1>
              <p className="mb-6">یادآوری: یکم فونت زشته و فاصله‌ی بین خطوط باید اصلاح بشه</p>
              <MainSearchbar/>
              <ul className="space-y-2 text-sm text-right" dir='rtl'>
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
          </motion.section>

          
          <motion.section 
            ref={refSecondSection}
            initial={{ x: -300, opacity: 0 }} 
            animate={inViewSecondSection ? { x: 0, opacity: 1 } : { x: -300, opacity: 0 }} 
            transition={{ duration: 1 }} 
            className="flex flex-col-reverse lg:flex-row lg:gap-4 items-center"
          >
            <div className="lg:w-1/2 pb-4">
              <div className="w-full rounded-lg overflow-hidden relative">
                <LiaChalkboardTeacherSolid style={{ fontSize: '550px', opacity: '0.15' }} className="w-full object-cover text-gray-400" />
                <FaUniversity 
                  style={{ 
                    fontSize: '300px', 
                    position: 'absolute', 
                    bottom: '10px',
                    right: '30px'
                  }} 
                  className="text-teal-800" 
                />
              </div>
            </div>
            <Signin/>
           
          </motion.section>

          <motion.section 
            ref={refTheardSection}
            initial={{ x: 300, opacity: 0 }} 
            animate={inViewTheardSection ? { x: 0, opacity: 1 } : { x: 300, opacity: 0 }} 
            transition={{ duration: 1 }} 
            className="flex flex-col-reverse lg:flex-row items-center"
            dir="rtl"
          >
            <div className="lg:w-1/2">
              <div className="w-full rounded-lg overflow-hidden relative">
                <TfiEmail style={{ fontSize: '500px', opacity: '0.15' }} className="w-full object-cover text-gray-400" />
                <MdOutlineAlternateEmail
                  style={{
                    fontSize: '300px',
                    position: 'absolute',
                    bottom: '10px',
                    right: '30px'
                  }}
                  className="text-teal-800 "
                />
              </div>
            </div>
            <div className="flex flex-col gap-2 items-start lg:w-1/2 p-4 text-center lg:text-right">
              <h1 className="text-4xl lg:leading-relaxed md:text-5xl lg:text-6xl font-bold mb-6">توضیحات متفرقه در تایتل این مجموعه</h1>
              <p className="mb-6">یادآوری: یکم فونت زشته و فاصله‌ی بین خطوط باید اصلاح بشه</p>
             <MainSearchbar/>
              
            </div>
          </motion.section>
        </main>
      </div>
    </div>
  );
}

export default Main;

