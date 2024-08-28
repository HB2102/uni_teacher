import React, { useState } from 'react';
import { IoMdArrowDropdown } from "react-icons/io";
import "./request.css";
import { motion } from 'framer-motion';
import BackButton from './BackButton';


const DefultRequest = () => {
    
        const variants = {
            hidden: { opacity: 0, y: 10 },
            visible: { opacity: 1, y: 0 }
          };
        
    

  const [email, setEmail] = useState(''); 
  const [requestText, setRequestText] = useState(''); 

  
  const handleEmailChange = (e) => setEmail(e.target.value);
  const handleRequestTextChange = (e) => setRequestText(e.target.value);

  return (
    <motion.section
    className="w-full lg:w-11/12"
    initial="hidden"
    animate="visible"
    exit="hidden"
    variants={variants}
    transition={{ duration: 0.5 }}
  >
    <div dir="rtl" className="container w-full flex flex-wrap mx-auto px-2 pt-8 lg:pt-16">

      {/* Section container */}
      <section className="w-full">
        {/* Section 2 */}
        <h2 id="section1" className="font-iran font-bold break-normal text-text-gray px-2 pb-8 text-xl">
          ثبت درخواست
        </h2>
        <div  className="p-8 mt-6 lg:mt-0 rounded shadow bg-white dark:bg-background-dark">
          <form>
            <div className="md:flex mb-6">
              <div className="md:w-1/6">
                <label
                  className="block text-gray-600 font-bold md:text-left mb-3 md:mb-0 pl-4" 
                  htmlFor="email-input"
                >
                  ایمیل شما
                </label>
              </div>
              <div className="md:w-5/6">
                <input
                  id="email-input"
                  className="w-full focus:bg-white h-11 rounded-md"
                  type="text"
                  value={email} 
                  onChange={handleEmailChange} 
                />
                <p className="py-2 text-sm text-gray-600">درصورت نیاز با شما ارتباط خواهیم گرفت</p>
              </div>
            </div>

            <div className="md:flex mb-6">
              <div className="md:w-1/6">
                <label
                  className="block text-gray-600 font-bold md:text-left mb-3 md:mb-0 pl-4" 
                  htmlFor="request-textarea"
                >
                  متن درخواست
                </label>
              </div>
              <div className="md:w-5/6">
                <textarea
                  id="request-textarea"
                  className="form-textarea block w-full focus:bg-white rounded-md"
                  rows="8"
                  value={requestText}
                  onChange={handleRequestTextChange} 
                ></textarea>
                <p className="py-2 text-sm text-gray-600"></p>
              </div>
            </div>

            <div dir='ltr' className="md:flex" >
             <BackButton ask={"defult"}/>
            </div> 
            
          </form>
        </div>
      </section>
    </div>
    </motion.section>
  );
};

export default DefultRequest;
