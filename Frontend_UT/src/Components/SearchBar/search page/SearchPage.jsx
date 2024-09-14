
import React, { useState, useEffect } from 'react'
import {AiOutlineSearch} from 'react-icons/ai'
import SwitchSearch from '../swichSearch'
import Searchbar from './Searchbar'
import ReviewCard from './Cards/TeacherCard'

const SearchPage = () => {
    const [searchAsk, setSearchAsk] = useState(0);
    const [searchResult, setSearchResult] = useState([]);


  return (
    <>
    <Searchbar searchAsk={searchAsk} setSearchResult={setSearchResult} searchResult={searchResult}/>
    <div dir='rtl' className="w-full flex items-center justify-center m-auto mt-11">
         <SwitchSearch setSearchAsk={setSearchAsk}  searchAsk={searchAsk} />
    </div>
  {
    searchAsk===1 ?
     <div className='flex flex-row gap-5 items-center justify-center flex-wrap '>
        {searchResult.map((result,key) => (
                    
                    <ReviewCard key={key} 
                    name={result.teacher.full_name}
                    Score={result.teacher.total_average_score}
                    comment={result.teacher.number_of_comments}
                    imageURL={result.teacher.teacher_pic}
                    subs={result.subjects}
                    unis={result.unis}/>
                    

                
        ))}
   
    </div>
:
null
  }
    

    
    </>
   
  )
}

export default SearchPage