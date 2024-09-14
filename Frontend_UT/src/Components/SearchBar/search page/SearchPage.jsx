import React, { useState, useEffect } from 'react';
import { AiOutlineSearch } from 'react-icons/ai';
import SwitchSearch from '../swichSearch';
import Searchbar from './Searchbar';
import ReviewCard from './Cards/TeacherCard';
import UniCards from './Cards/UniCards';
import SubjectCards from './Cards/SubjectCards';
import { useNavigate } from 'react-router-dom';
const SearchPage = () => {
    const navigate = useNavigate();
    const [searchAsk, setSearchAsk] = useState(1);
    const [searchResult, setSearchResult] = useState([]);

    useEffect(() => {
        Clear();
    }, [searchAsk]); 

    const Clear = () => {
        setSearchResult([]);
    };
    const handleBackHome = ()=> {
        navigate("/");
      }

    return (
        <>
      
            <Searchbar searchAsk={searchAsk} setSearchResult={setSearchResult} searchResult={searchResult} />
          
            <div dir="rtl" className="w-full flex items-center justify-center m-auto mt-11">
                <SwitchSearch setSearchAsk={setSearchAsk} searchAsk={searchAsk} />
            </div>
            {searchAsk === 1 ? (
                <div className='flex flex-row gap-5 items-center justify-center flex-wrap'>
                    {searchResult.length > 0 ? 
                     searchResult.map((result, key) => (
                        result.teacher && (
                            <ReviewCard                         
                                key={key}
                                name={result.teacher.full_name}
                                Score={result.teacher.total_average_score}
                                comment={result.teacher.number_of_comments}
                                imageURL={result.teacher.teacher_pic}
                                subs={result.subjects}
                                unis={result.unis}
                            />
                        )
                    ))
                    
                    : null}
                </div>
            ) : null}
            {searchAsk === 2 ? (
                <div className='flex flex-row gap-5 items-center justify-center flex-wrap'>
                    {searchResult.length > 0 ?
                    searchResult.map((result, key) => (
                        <UniCards                         
                            key={key}
                            name={result.name}
                            id={result.id}
                        />
                    )) : null}
                </div>
            ) : null}
            {searchAsk === 3 ? (
                <div className='flex flex-row gap-5 items-center justify-center flex-wrap'>
                    {searchResult.length > 0 ?
                    searchResult.map((result, key) => (
                        <SubjectCards                         
                            key={key}
                            name={result.name}
                            id={result.id}
                        />
                    )) : null}
                </div>
            ) : null}
              <div onClick={handleBackHome} dir='rtl' className="w-full flex h-full items-end  lg:w-4/5 lg:mr-auto text-base md:text-sm text-gray-600 px-4 pt-5"> {/* Changed margin from left to right */}
          <span className="text-base text-teal-600 font-bold">&lt;</span>{' '}
          <a  className="text-base md:text-sm text-teal-600 font-bold no-underline hover:underline">
            بازگشت به صفحه‌ی اصلی
          </a>
        </div>
        </>
    );
};

export default SearchPage;
