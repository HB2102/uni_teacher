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
function Main() {
  const [isMenuOpen, setIsMenuOpen] = useState(false);


  const handleClickLogin = () => {
    setIsMenuOpen(true);
  };

  const { ref: refFirstSection, inView: inViewFirstSection } = useInView({
    triggerOnce: true, 
    threshold: 0,
  });
  const { ref: refTheardSection, inView: inViewTheardSection } = useInView({
    triggerOnce: true, 
    threshold: 0, 
  });
  // Use the useInView hook for the second section
  const { ref: refSecondSection, inView: inViewSecondSection } = useInView({
    triggerOnce: true,
    threshold: 0,
  });

  return (
    <div className="min-h-screen bg-gray-900 text-white flex flex-col items-center justify-center p-4">
      <div style={{ minHeight: 'calc(100vh - 60px)' }}>      
        <main className="flex flex-col gap-4 w-full max-w-7xl mt-6 sm:py-5 md:py-22 lg:py-22 xl:py-18">
          
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
              <div className="flex w-full mb-4 flex-col sm:flex-row">
                <button className="bg-teal-500 px-6 py-3 rounded-full text-white hover:bg-teal-600">جستجو</button>
                <input
                  type="text"
                  placeholder="دنبال چی میگردی؟"
                  className="lg:w-2/3 p-3 placeholder:text-gray-500 placeholder:pr-4 rounded-full text-black mb-3 sm:mb-0 sm:mr-2 text-right bg-slate-200"
                />
              </div>
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
            className="flex flex-col-reverse lg:flex-row items-center"
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
            {isMenuOpen===true ? <Signin/> : <div className="space-y-2 lg:w-1/2 text-right text-4xl md:text-5xl lg:text-3xl font-bold mb-6" dir='rtl'>
 
 <p className="flex items-center pb-5 leading-relaxed">
     
     عاهرذسصخدص
      <br/>
     با داشتن حساب کاربری از امکانات بیشتری<br/> بهره‌مند شوید
 </p> 
 <button onClick={handleClickLogin} className="bg-teal-500  text-xl px-6 py-2 rounded-full text-white hover:bg-teal-600">ورود/ثبت نام</button>
 </div> }
           
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
              <div className="flex w-full mb-4 flex-col sm:flex-row">
                <button className="bg-teal-500 px-6 py-3 rounded-full text-white hover:bg-teal-600">جستجو</button>
                <input
                  type="text"
                  placeholder="دنبال چی میگردی؟"
                  className="lg:w-2/3 p-3 placeholder:text-gray-500 placeholder:pr-4 rounded-full text-black mb-3 sm:mb-0 sm:mr-2 text-right bg-slate-200"
                />
              </div>
              
            </div>
          </motion.section>
        </main>
      </div>
    </div>
  );
}

export default Main;
