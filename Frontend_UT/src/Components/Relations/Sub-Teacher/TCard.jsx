import React from 'react';
import { FaRegComments } from "react-icons/fa6";
import { useNavigate } from 'react-router-dom';

const TCard = ({name , Score , comment , imageURL }) => {
    const navigate = useNavigate();
    const handleSendRequest=() =>{
        navigate("/request");
      }

  return (
    <article dir='rtl' className="farmer-motion p-5 bg-white dark:bg-gray-800 rounded-lg shadow-md w-10/12 sm:w-[48%] md:w-[48%] lg:w-1/4 xl:w-1/5 mt-9">
      <div dir='rtl' className="flex items-center mb-4">
        <img
          className="w-10 h-10 ml-4 rounded-full"
          src={imageURL}
          alt="Profile"
        />
        <div className="font-medium dark:text-white">
          <h2>
            {name} {' '}
           
          </h2>
        </div>
      </div>
      <div className="flex items-center mb-1 space-x-1">
        {[...Array({Score})].map((_, index) => (
          <svg
            key={index}
            className="w-4 h-4 text-yellow-300"
            aria-hidden="true"
            xmlns="http://www.w3.org/2000/svg"
            fill="currentColor"
            viewBox="0 0 22 20"
          >
            <path d="M20.924 7.625a1.523 1.523 0 0 0-1.238-1.044l-5.051-.734-2.259-4.577a1.534 1.534 0 0 0-2.752 0L7.365 5.847l-5.051.734A1.535 1.535 0 0 0 1.463 9.2l3.656 3.563-.863 5.031a1.532 1.532 0 0 0 2.226 1.616L11 17.033l4.518 2.375a1.534 1.534 0 0 0 2.226-1.617l-.863-5.03L20.537 9.2a1.523 1.523 0 0 0 .387-1.575Z" />
          </svg>
        ))}
        <svg
          className="w-4 h-4 text-gray-300 dark:text-gray-500"
          aria-hidden="true"
          xmlns="http://www.w3.org/2000/svg"
          fill="currentColor"
          viewBox="0 0 22 20"
        >
          <path d="M20.924 7.625a1.523 1.523 0 0 0-1.238-1.044l-5.051-.734-2.259-4.577a1.534 1.534 0 0 0-2.752 0L7.365 5.847l-5.051.734A1.535 1.535 0 0 0 1.463 9.2l3.656 3.563-.863 5.031a1.532 1.532 0 0 0 2.226 1.616L11 17.033l4.518 2.375a1.534 1.534 0 0 0 2.226-1.617l-.863-5.03L20.537 9.2a1.523 1.523 0 0 0 .387-1.575Z" />
        </svg>
      </div>

      <aside dir='ltr'>
        <a  className="mt-1 text-xs text-gray-500 dark:text-gray-400">
       کامنت
        </a>
        <button  className="mt-1 ml-1 text-xs text-gray-500 dark:text-gray-400">
        { comment  } 
        </button>
        <div className="flex items-center mt-3">
          <a
            href="#"
            className="px-3 py-2 text-xs font-medium text-gray-900 bg-white border border-gray-200 rounded-lg hover:bg-gray-100 hover:text-blue-700 focus:z-10 focus:outline-none focus:ring-4 focus:ring-gray-100 dark:focus:ring-gray-700 dark:bg-gray-800 dark:text-gray-400 dark:border-gray-600 dark:hover:text-white dark:hover:bg-gray-700"
          >
         پروفایل استاد
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

export default TCard;
