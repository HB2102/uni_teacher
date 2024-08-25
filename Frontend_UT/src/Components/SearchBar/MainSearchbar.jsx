// محتوای این صفحه نیاز به بازنویسی دارد
import React, { useState } from 'react'
import {AiOutlineSearch} from 'react-icons/ai'

const words=[
    'sara',
    'mamad',
    'mamadali',
    'samad',
    'eli'
]
//  محتوای این صفحه نیاز به بازنویسی دارد
const MainSearchbar = () => {

    const [activeSearch, setActiveSearch] = useState([])

    const handleSearch = (e) => {
        if(e.target.value == ''){
            setActiveSearch([])
            return false
        }
        setActiveSearch(words.filter(w => w.includes(e.target.value)).slice(0,8))
    }

  return (
    <div>
        <div className="flex w-full mb-4 flex-col sm:flex-row">
      <button className="bg-teal-500 px-6 py-3 rounded-full text-white hover:bg-teal-600">جستجو</button>
      <input
        type="text"
        placeholder="دنبال چی میگردی؟"
        className="lg:w-2/3 p-3 placeholder:text-gray-500 rounded-full text-black mb-3 sm:mb-0 sm:mr-2 text-right bg-slate-200"
        onChange={(e) => handleSearch(e)}
      />
       {
            activeSearch.length > 0 && (
                <div className="absolute top-20 p-4 bg-slate-800 text-white w-full rounded-xl left-1/2 -translate-x-1/2 flex flex-col gap-2">
                    {
                        activeSearch.map(s => (
                            <span>{s}</span>
                        ))
                    }
                </div>
            )
        }
    </div>

   
    </div>

  )
}

export default MainSearchbar

