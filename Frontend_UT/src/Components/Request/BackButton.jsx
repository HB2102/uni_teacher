import React, { useState } from 'react';
import { IoMdArrowDropdown } from "react-icons/io";
import "./request.css";
import { motion } from 'framer-motion';
import { useNavigate } from 'react-router-dom';


const BackButton = ({ask}) => {
    const navigate = useNavigate();
    const handleClick=()=>{
        console.log(ask);
    }

  return (   
              <div className="md:w-full">
                <button
                onClick={handleClick}
                  className="shadow bg-yellow-700 hover:bg-yellow-500 focus:shadow-outline focus:outline-none text-white font-bold py-2 px-8 rounded pt-3"
                  type="button"
                >
                  ارسال درخواست
                </button>
              </div>
  );
};

export default BackButton;
