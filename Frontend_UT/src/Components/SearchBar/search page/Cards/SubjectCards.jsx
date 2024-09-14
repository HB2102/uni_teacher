import React from 'react';
import { FaRegComments } from "react-icons/fa6";
import { useNavigate } from 'react-router-dom';
import { FaChalkboardTeacher } from "react-icons/fa";
import '../search.css'
const SubjectCards = ({name,id}) => {
    const navigate = useNavigate();
    const handleSendRequest=() =>{
        navigate("/request");
      }

  return (
    <article dir='rtl' className="farmer-motion p-5 bg-white dark:bg-gray-800 rounded-lg shadow-md w-10/12 sm:w-[48%] md:w-[48%] lg:w-1/4 xl:w-1/5 mt-9">
      <div dir='rtl' className="flex items-center mb-4">
        <FaChalkboardTeacher
          className="w-10 h-10 ml-4 "
         
        />
        <div className="font-medium dark:text-white">
          <h2>
            {name} {' '}
           
          </h2>
        </div>
      </div>
     
     
      <aside dir='ltr'>
    
        <div className="flex items-center mt-3">
          <a
            href="#"
            className="px-3 py-2 text-xs font-medium text-gray-900 bg-white border border-gray-200 rounded-lg hover:bg-gray-100 hover:text-blue-700 focus:z-10 focus:outline-none focus:ring-4 focus:ring-gray-100 dark:focus:ring-gray-700 dark:bg-gray-800 dark:text-gray-400 dark:border-gray-600 dark:hover:text-white dark:hover:bg-gray-700"
          >
         جزئیات بیشتر
          </a>
          <button
          onClick={handleSendRequest}
            className="pl-4 ml-4 text-sm font-medium text-blue-600 border-l border-gray-200 hover:underline dark:text-blue-500 dark:border-gray-600"
          >
           ثبت گزارش
          </button>
        </div>
      </aside>
    </article>
  );
};

export default SubjectCards;
