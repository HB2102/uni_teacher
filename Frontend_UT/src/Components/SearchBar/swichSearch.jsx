import React, { useState } from 'react';

const SwitchSearch = ({ setSearchAsk , searchAsk,setSearchAsk2 }) => {
    const handleAsks=(value)=>{
        switch (value) {
            case 1:
                setSearchAsk(1)
                setSearchAsk2(1)
                break;
            case 2:
                setSearchAsk(2)
                setSearchAsk2(2)
                break;
             case 3:
                setSearchAsk(3)
                setSearchAsk2(3)
                break;    
            default:
                break;
        }
    }
    return (
        <div className="">
            <div className="sm:w-fit xs:w-[90%] sm:px-4 py-2 rounded-sm flex md:flex-no-wrap xs:flex-wrap md:gap-4 xs:gap-1 justify-center  text-white dark:text-black cursor-pointer md:text-lg md:font-semibold xs:text-sm">
                <div className="px-4 cursor-default dark:hover:border-blue-500 rounded-b-md">
                    جستجو :
                </div>
  
                <div
                    className={`px-4 hover:border-b-2  dark:border-blue-500 hover:border-teal-600 rounded-b-md   ${
                        searchAsk === 1 ? 'border-teal-600 border-b-2' : ''
                    }`}
                    onClick={() => handleAsks(1)}
                >
                    اساتید
                </div>

               
                <div
                    className={`px-4 hover:border-b-2 dark:hover:border-blue-500 hover:border-teal-600 rounded-b-md ${
                        searchAsk === 2 ? 'border-teal-600 border-b-2' : ''
                    }`}
                    onClick={() => handleAsks(2)}
                >
                    دانشگاه‌ها
                </div>

                <div
                    className={`px-4 hover:border-b-2 dark:border-blue-500 hover:border-teal-600 rounded-b-md   ${
                        searchAsk === 3 ? 'border-teal-600 border-b-2' : ''
                    }`}
                    onClick={() => handleAsks(3)}
                >
                    دروس
                </div>
            </div>
        </div>
    );
};

export default SwitchSearch;
