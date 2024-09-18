import React, { useState, useEffect } from 'react';
import { IoMdArrowDropdown } from "react-icons/io";
const TeacherRate = () => {

 return( 
     <section className="pt-12 relative">
    <div className="w-full max-w-7xl px-4 md:px-5 lg:px-6 mx-auto">
      <div className="">
        <div className="grid grid-cols-12 mb-11">
          {/* Left Column */}
          <div className="col-span-12 xl:col-span-4 flex items-center">
            <div className="flex flex-col gap-y-4 w-full max-xl:max-w-3xl mx-auto">
              {/** Rating bars */}
              {[5, 4, 3, 2, 1].map((rating, index) => (
                <div className="flex items-center w-full" key={index}>
                  <p className="font-medium text-lg py-[1px] text-black mr-[2px]">{rating}</p>
                  <svg
                    width="20"
                    height="20"
                    viewBox="0 0 20 20"
                    fill="none"
                    xmlns="http://www.w3.org/2000/svg"
                  >
                    <g clipPath="url(#clip0_12042_8589)">
                      <path
                        d="M9.10326 2.31699C9.47008 1.57374 10.5299 1.57374 10.8967 2.31699L12.7063 5.98347C12.8519 6.27862 13.1335 6.48319 13.4592 6.53051L17.5054 7.11846C18.3256 7.23765 18.6531 8.24562 18.0596 8.82416L15.1318 11.6781C14.8961 11.9079 14.7885 12.2389 14.8442 12.5632L15.5353 16.5931C15.6754 17.41 14.818 18.033 14.0844 17.6473L10.4653 15.7446C10.174 15.5915 9.82598 15.5915 9.53466 15.7446L5.91562 17.6473C5.18199 18.033 4.32456 17.41 4.46467 16.5931L5.15585 12.5632C5.21148 12.2389 5.10393 11.9079 4.86825 11.6781L1.94038 8.82416C1.34687 8.24562 1.67438 7.23765 2.4946 7.11846L6.54081 6.53051C6.86652 6.48319 7.14808 6.27862 7.29374 5.98347L9.10326 2.31699Z"
                        fill="#FBBF24"
                      />
                    </g>
                  </svg>
                  <p className="h-2 w-full sm:min-w-[278px] rounded-[30px] bg-gray-200 ml-5 mr-3">
                    <span
                      className={`h-full ${
                        rating === 5 ? 'w-[30%]' : rating === 4 ? 'w-[40%]' : rating === 3 ? 'w-[20%]' : rating === 2 ? 'w-[16%]' : 'w-[8%]'
                      } rounded-[30px] bg-indigo-500 flex`}
                    ></span>
                  </p>
                  <p className="font-medium text-lg py-[1px] text-black mr-[2px]">{rating * 10}</p>
                </div>
              ))}
            </div>
          </div>
          {/* Right Column */}
          <div className="col-span-12 max-xl:mt-8 xl:col-span-8 xl:pl-8 w-full min-h-[230px]">
            <div className="grid grid-cols-12 h-full px-8 max-lg:py-8 rounded-3xl bg-gray-100 w-full max-xl:max-w-3xl max-xl:mx-auto">
              درس ها و دانشگاه های استاد
            </div>
          </div>
        </div>
   
      </div>
    </div>
  </section> )}
  
  export default TeacherRate;