import React, { useState,useEffect } from 'react';
import { AiOutlineSearch } from 'react-icons/ai';
import "./MainSearch.css";
import axios from 'axios';
const MainSearchbar = ({ searchAsk }) => {
  const [activeSearch, setActiveSearch] = useState([]);
  const [words, setWords] = useState([]);
  const [searchInput, setSearchInput] = useState('');  // State for capturing user input
  useEffect(() => {
    handleAllData()
  }, [searchAsk])
  useEffect(() => {
    Clear();
  }, [searchAsk]);

  useEffect(() => {
    if (searchInput !== '') {
      handleSubmit(); // Automatically submit the form when searchInput is set via ResultClick
    }
  }, [searchInput]);


  const Clear=()=>{
    setSearchInput('')
    }
const logclick=(s)=>{
  setSearchInput(s);

    setActiveSearch('')
}

  const handleSearch = (e) => {
    setSearchInput(e.target.value);
    if (e.target.value === '') {
      setActiveSearch([]);
      return false;
    }
    setActiveSearch(words.filter((w) => w.includes(e.target.value)).slice(0, 8));
  };

  const handleAllData= async()=>{
    switch (searchAsk) {
      case 1:
        try {
          const response = await axios.get('http://127.0.0.1:8000/teacher/get_all_teachers');
          // console.log('Search result:', response.data);
          const  transformedWords = response.data.map(obj => obj.full_name);
          setWords(transformedWords)
          } catch (error) {
            console.log('Error fetching search results:', error);
          }
      break;
      case 2:
          try {
            const response = await axios.get('http://127.0.0.1:8000/university/get_all_uni');
            // console.log('Search result:', response.data);
            const  transformedWords = response.data.map(obj => obj.name);
            setWords(transformedWords)
            } catch (error) {
              console.log('Error fetching search results:', error);
            }
        break;
        case 3:
          try {
            const response = await axios.get('http://127.0.0.1:8000/subject/get_all_subjects');
            // console.log('Search result:', response.data);
            const  transformedWords = response.data.map(obj => obj.name);
            setWords(transformedWords)
            } catch (error) {
              console.log('Error fetching search results:', error);
            }
        break;
    
      default:
        // console.log("choose an option stupid !");
        break;
    }
  }
  const handleSubmit = async (e) => {
    if (e) e.preventDefault();
    console.log(searchInput);
    
  };

  return (
    <form className="w-full relative" onSubmit={handleSubmit}>
      <div className="flex mb-4 flex-col relative sm:flex-row">
        <button className="bg-teal-700 px-6 py-3 sm:rounded-s-full rounded-none text-white hover:bg-teal-900">جستجو</button>
        <div className="relative w-full lg:w-2/3"> 
          <input
            type="text"
            placeholder="دنبال چی میگردی؟"
            className="css w-full p-3 placeholder:text-gray-500 placeholder:pr-1 sm:rounded-e-full rounded-none text-black mb-3 sm:mb-0 sm:mr-0 text-right bg-slate-200"
            value={searchInput}
            onChange={(e) => handleSearch(e)}
          />
          {activeSearch.length > 0 && (
            <div className="absolute top-full left-0 right-0 mt-1 p-4 bg-slate-800 text-white rounded-xl flex flex-col gap-2"> 
              {activeSearch.map((s, index) => (
                <span onClick={()=>logclick(s)} key={index}>{s}</span>
              ))}
            </div>
          )}
        </div>
      </div>
    </form>
  );
};

export default MainSearchbar;
