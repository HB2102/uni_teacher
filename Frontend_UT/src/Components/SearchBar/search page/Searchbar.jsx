import React, { useState, useEffect } from 'react';
import { AiOutlineSearch } from 'react-icons/ai';
import axios from 'axios';

const Searchbar = ({  searchAsk , setSearchResult ,searchResult }) => {
  const [activeSearch, setActiveSearch] = useState([]);
  const [words, setWords] = useState([]);
  const [searchInput, setSearchInput] = useState('');

  useEffect(() => {
    handleAllData();
  }, [searchAsk]);

  useEffect(() => {
    Clear();
  }, [searchAsk]);


  const ResultClick = (s) => {
    setSearchInput(s);
    setActiveSearch('')
  };
    const Clear=()=>{
    setSearchInput('')
    }
  const handleSearch = (e) => {
    setSearchInput(e.target.value);
    if (e.target.value === '') {
      setActiveSearch([]);
      return false;
    }
    setActiveSearch(words.filter((w) => w.includes(e.target.value)).slice(0, 8));
  };

  const handleAllData = async () => {
    switch (searchAsk) {
      case 1:
        try {
          const response = await axios.get('http://127.0.0.1:8000/teacher/get_all_teachers');
          const transformedWords = response.data.map((obj) => obj.full_name);
          setWords(transformedWords);
        } catch (error) {
          console.log('Error fetching search results:', error);
        }
        break;
      case 2:
        try {
          const response = await axios.get('http://127.0.0.1:8000/university/get_all_uni');
          const transformedWords = response.data.map((obj) => obj.name);
          setWords(transformedWords);
        } catch (error) {
          console.log('Error fetching search results:', error);
        }
        break;
      case 3:
        try {
          const response = await axios.get('http://127.0.0.1:8000/subject/get_all_subjects');
          const transformedWords = response.data.map((obj) => obj.name);
          setWords(transformedWords);
        } catch (error) {
          console.log('Error fetching search results:', error);
        }
        break;
      default:
        break;
    }
  };

  const handleSubmit = async (e) => {
    if (e) e.preventDefault();
    
    switch (searchAsk) {
      case 1:
        try {
            const response = await axios.post(
              'http://127.0.0.1:8000/teacher/search_teacher_name',
              {
                teacher_name: searchInput,
              },
              {
                headers: {
                  'Content-Type': 'application/json',
                  Accept: 'application/json',
                },
              }
            );
            setSearchResult(response.data)
            console.log(response.data);  
            setActiveSearch('')
          } catch (error) {
            console.log('Error searching university:', error);
          }
        break;
      case 2:
        try {
          const response = await axios.post(
            'http://127.0.0.1:8000/university/search_uni',
            {
              uni_name: searchInput,
            },
            {
              headers: {
                'Content-Type': 'application/json',
                Accept: 'application/json',
              },
            }
          );
          console.log(response);
        } catch (error) {
          console.log('Error searching university:', error);
        }
        break;
      case 3:
        try {
          const response = await axios.post(
            'http://127.0.0.1:8000/subject/search_subject',
            {
              subject_name: searchInput,
            },
            {
              headers: {
                'Content-Type': 'application/json',
                Accept: 'application/json',
              },
            }
          );
          setSearchResult(response.data)
          console.log(searchResult);
          
        } catch (error) {
          console.log('Error searching subject:', error);
        }
        break;
      default:
        break;
    }
  };

  return (
    <>
      <form className='lg:w-3/5 md:w-10/12 relative m-auto mt-12' onSubmit={handleSubmit}>
        <div className="relative">
          <input
            type="search"
            placeholder='دنبال چی میگردی؟'
            className='placeholder:p-3 placeholder:text-gray-700 w-full p-4 rounded-full bg-slate-200'
            value={searchInput}
            onChange={handleSearch}
          />
          <button type="submit" className='absolute right-1 top-1/2 -translate-y-1/2 p-4 bg-gray-600 rounded-full'>
            <AiOutlineSearch />
          </button>
        </div>

        {activeSearch.length > 0 && (
          <div className="absolute top-16 p-4 bg-slate-800 text-white w-full rounded-xl left-1/2 -translate-x-1/2 flex flex-col gap-2">
            {activeSearch.map((s, index) => (
              <span onClick={() => ResultClick(s)} key={index}>
                {s}
              </span>
            ))}
          </div>
        )}
      </form>
    </>
  );
};

export default Searchbar;
