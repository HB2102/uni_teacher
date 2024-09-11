import React, { useState } from 'react';
import { AiOutlineSearch } from 'react-icons/ai';
import "./MainSearch.css";
const words = ['sara', 'mamad', 'mamadali', 'samad', 'eli'];

const MainSearchbar = () => {
  const [activeSearch, setActiveSearch] = useState([]);
const logclick=()=>{
  console.log("nsndhdcbsdh");
  
}
  const handleSearch = (e) => {
    if (e.target.value === '') {
      setActiveSearch([]);
      return false;
    }
    setActiveSearch(words.filter((w) => w.includes(e.target.value)).slice(0, 8));
  };

  return (
    <form className="w-full relative">
      <div className="flex mb-4 flex-col relative sm:flex-row">
        <button className="bg-teal-500 px-6 py-3 rounded-s-full text-white hover:bg-teal-600">جستجو</button>
        <div className="relative w-full lg:w-2/3"> 
          <input
            type="text"
            placeholder="دنبال چی میگردی؟"
            className="css w-full p-3 placeholder:text-gray-500 placeholder:pr-1 rounded-e-full text-black mb-3 sm:mb-0 sm:mr-0 text-right bg-slate-200"
            onChange={(e) => handleSearch(e)}
          />
          {activeSearch.length > 0 && (
            <div className="absolute top-full left-0 right-0 mt-1 p-4 bg-slate-800 text-white rounded-xl flex flex-col gap-2"> 
              {activeSearch.map((s, index) => (
                <span onClick={logclick} key={index}>{s}</span>
              ))}
            </div>
          )}
        </div>
      </div>
    </form>
  );
};

export default MainSearchbar;
