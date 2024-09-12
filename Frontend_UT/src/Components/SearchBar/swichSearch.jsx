import React, { useState } from 'react';

const SwitchSearch = ({ setSearchAsk , searchAsk }) => {
    return (
        <div className="">
            <div className="sm:w-fit xs:w-[90%] sm:px-4 py-2 rounded-sm flex md:flex-no-wrap xs:flex-wrap md:gap-4 xs:gap-1 justify-center dark:bg-gray-200 text-white dark:text-black cursor-pointer md:text-lg md:font-semibold xs:text-sm">
                <div className="px-4 cursor-default dark:hover:border-blue-500 rounded-b-md">
                    جستجو میان :
                </div>
  
                <div
                    className={`px-4 hover:border-b-2  dark:border-blue-500 hover:border-teal-600 rounded-b-md   ${
                        searchAsk === 1 ? 'border-teal-600 border-b-2' : ''
                    }`}
                    onClick={() => setSearchAsk(1)}
                >
                    اساتید
                </div>

               
                <div
                    className={`px-4 hover:border-b-2 dark:hover:border-blue-500 hover:border-teal-600 rounded-b-md ${
                        searchAsk === 2 ? 'border-teal-600 border-b-2' : ''
                    }`}
                    onClick={() => setSearchAsk(2)}
                >
                    دانشگاه‌ها
                </div>

                <div
                    className={`px-4 hover:border-b-2 dark:border-blue-500 hover:border-teal-600 rounded-b-md   ${
                        searchAsk === 3 ? 'border-teal-600 border-b-2' : ''
                    }`}
                    onClick={() => setSearchAsk(3)}
                >
                    دروس
                </div>
            </div>
        </div>
    );
};

export default SwitchSearch;
