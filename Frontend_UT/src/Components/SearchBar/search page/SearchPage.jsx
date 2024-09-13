
import React, { useState } from 'react'
import {AiOutlineSearch} from 'react-icons/ai'
import SwitchSearch from '../swichSearch'
import Searchbar from './Searchbar'

const SearchPage = () => {
    const [searchAsk, setSearchAsk] = useState(0);
 



  return (
    <>
    <Searchbar searchAsk={searchAsk}/>
    <div dir='rtl' className="w-full flex items-center justify-center m-auto mt-11">
         <SwitchSearch setSearchAsk={setSearchAsk} searchAsk={searchAsk}/>
    </div>


    
    </>
   
  )
}

export default SearchPage