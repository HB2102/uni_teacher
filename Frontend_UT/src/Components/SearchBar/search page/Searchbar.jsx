'use client'

import React, { useState } from 'react'
import {AiOutlineSearch} from 'react-icons/ai'
import MainSearchbar from '../MainSearchbar'

const words=[
    'sara',
    'mamad',
    'mamadali',
    'samad',
    'eli'
]

const Searchbar = () => {

    const [activeSearch, setActiveSearch] = useState([])

    const handleSearch = (e) => {
        if(e.target.value == ''){
            setActiveSearch([])
            return false
        }
        setActiveSearch(words.filter(w => w.includes(e.target.value)).slice(0,8))
    }

  return (
    <>
     <form className='lg:w-3/5 md:w-10/12 relative m-auto mt-12 ' >
        <div className="relative">
            <input type="search" placeholder='دنبال چی میگردی؟' className='placeholder:p-12 placeholder:text-gray-700 w-full p-4 rounded-full bg-slate-300' onChange={(e) => handleSearch(e)}/>
            <button className='absolute right-1 top-1/2 -translate-y-1/2 p-4 bg-slate-600 rounded-full'>
                <AiOutlineSearch />
            </button>
        </div>

        {
            activeSearch.length > 0 && (
                <div className="absolute top-16 p-4 bg-slate-800 text-white w-full rounded-xl left-1/2 -translate-x-1/2 flex flex-col gap-2">
                    {
                        activeSearch.map(s => (
                            <span>{s}</span>
                        ))
                    }
                </div>
            )
        }


        
    </form>

    
    </>
   
  )
}

export default Searchbar