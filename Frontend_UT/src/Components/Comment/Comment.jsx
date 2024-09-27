import React, { useState, useEffect } from 'react';
import { BiLike,BiDislike  } from "react-icons/bi";
import { TbMessageReport } from "react-icons/tb";
import { CgProfile } from "react-icons/cg";
import axios from 'axios';
const SingleComment = ({teacher_id}) => {
    const [likeNumber, setLikeNumber] = useState(0);
    const [dislikeNumber, setDisLikeNumber] = useState(0);
    const [response, setResponse] = useState([]);
   
      useEffect(() => {
        const handleAllData = async () => {
            try {
                const response1 = await axios.post(
                    'http://127.0.0.1:8000/comment/get_all_comments_of_teacher',
                    {
                      teacher_id: teacher_id,
                      order:""
                    },
                    {
                      headers: {
                        'Content-Type': 'application/json',
                        Accept: 'application/json',
                      },
                    }
                  );
          
              setResponse(response1.data);
              console.log(response1);
              
            } catch (error) {
              console.log('Error fetching search results:', error);
            }
           
      };
        handleAllData();
      }, []);
    
    
    return (
        
        <section dir='rtl'  className="py-4 w-4/5 m-auto">
                     {response.length !== 0 && response.map((result, key) => (
                    <div key={key} className="swiper-slide group bg-white border border-solid border-gray-300 rounded-2xl max-sm:max-w-sm max-sm:mx-auto p-6 transition-all duration-500 hover:border-indigo-600">
                    <div className="flex items-center gap-5 mb-5 sm:mb-9">
                        {/* <img className="rounded-full object-cover" src="https://pagedone.io/asset/uploads/1696229969.png" alt="avatar"> */}
                        <CgProfile className='w-16 h-16' />
                        {/* <img
                        src="https://pagedone.io/asset/uploads/1696229969.png"
                            alt="avatar"
                            className="rounded-full object-cover"
                        /> */}
                        <div className="grid gap-1">
                        <div class="flex items-center flex-1  font-bold leading-tight">{result.username}
                             <span class="mr-2 text-xs font-normal text-gray-500">دو هفته قبل</span>
                         </div>
                            <span className="text-sm leading-6 text-gray-500">2 weeks ago </span>
                        </div>
                    </div>
              
                    <p 
                        className="text-lg text-gray-700 leading-6 transition-all duration-500 min-h-24 group-hover:text-gray-900">
                            {result.text}
                    </p>
                    <div className="flex items-center mb-3 sm:mb-9 gap-5  transition-all duration-500 mt-0">
                         <button className="flex flex-row gap-1 hover:text-sky-800 duration-300">
                             <span className='pt-1'> {dislikeNumber}</span>
                             <BiDislike className='w-7 h-7 ' />
                         </button>
                         <button className="flex flex-row gap-1 hover:text-sky-800 duration-300">
                             <span className='pt-2'> {likeNumber}</span>
                             <BiLike className='w-7 h-7  ' />   
                         </button>
                         <TbMessageReport className='w-7 h-7 hover:text-red-600 duration-300' />
                    </div>
                </div>
                  ))}
                   
        </section>
    );
};

export default SingleComment;
