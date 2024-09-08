import React, { useState } from 'react';
import { IoMdArrowDropdown } from "react-icons/io";
import "./request.css";
import axios from 'axios';
import Swal from "sweetalert2";  
import { motion } from 'framer-motion';
import { useNavigate } from 'react-router-dom';

const DefultRequest = () => {
  const navigate = useNavigate();
        const variants = {
            hidden: { opacity: 0, y: 10 },
            visible: { opacity: 1, y: 0 }
          };
        
        

  const [phone_number, setPhone_number] = useState(''); 
  const [requestText, setRequestText] = useState(''); 

  
  const handlePhoneNumberChange = (e) => setPhone_number(e.target.value);
  const handleRequestTextChange = (e) => setRequestText(e.target.value);
  const handleClick = async () => {
    console.log("Submitting request");
    try {
      const response = await axios.post('http://127.0.0.1:8000/request/send_request', 
        {
          text: requestText, 
          phone_number: phone_number 
        }, 
        {
          headers: { 'Content-Type': 'application/json' }
        }
      );
  
      if (response.status === 200) {
        Swal.fire({
          position: "top-end",
          title: "ارسال شد",
          showConfirmButton: false,
          timerProgressBar: true,
          timer: 2000,
          background: '#ffffff', 
          width: '400px',
          padding: '0.5em', 
          customClass: {
              title: 'small-alert-title', 
          },
          didOpen: () => {
              const progressBar = Swal.getTimerProgressBar();
              progressBar.style.backgroundColor = '#00ff00'; 
              progressBar.style.height = '3px';
              progressBar.style.width = '100%'; 
          }
      });
      
      
  
        setPhone_number('');  
        setRequestText('');
      }
    } catch (error) {
      if (error.response) {
        console.log('Validation error details:', error.response.data); 
      } else {
        console.log('Error:', error.message);
      }
    }
  };
  
  
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
        <h2 id="section1" className="font-iran font-bold break-normal text-text-gray px-2 pb-8 text-xl">
          ثبت درخواست
        </h2>
        <div  className="p-8 mt-6 lg:mt-0 rounded shadow bg-white dark:bg-background-dark">
          <form>
            <div className="md:flex mb-6">
              <div className="md:w-1/6">
                <label
                  className="block text-gray-600 font-bold md:text-left mb-3 md:mb-0 pl-4" 
                  htmlFor="phone_number-input"
                >
                 شماره موبایل
                </label>
              </div>
              <div className="md:w-5/6">
                <input
                  id="phone_number-input"
                  className="w-full focus:bg-white h-11 rounded-md"
                  type="text"
                  value={phone_number} 
                  onChange={handlePhoneNumberChange} 
                />
                <p className="py-2 text-sm text-gray-600">نتیجه‌ي بررسی درخواست به شما اطلاع داده می‌شود</p>
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
            <div className="md:w-full">
                <button
                onClick={handleClick}
                  className="shadow bg-teal-700 hover:bg-teal-500 focus:shadow-outline focus:outline-none text-white font-bold py-2 px-8 rounded pt-3"
                  type="button"
                >
                  ارسال درخواست
                </button>
              </div>
            </div> 
            
          </form>
        </div>
      </section>
    </div>
    </motion.section>
  );
};

export default DefultRequest;
