import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import { useLocation } from 'react-router-dom';
import axios from 'axios';
import ReviewCard from '../../SearchBar/search page/Cards/TeacherCard';
import TCard from './TCard';
import { Button } from 'bootstrap';

const SubjectTeachers = () => {
    const navigate = useNavigate();
    const location = useLocation();
    const [subject_id, setSubjectId] = useState(-1);
    const [data,setData]=useState([])
    useEffect(() => {
        if (location.state && location.state.subject_id) {
            setSubjectId(location.state.subject_id); 
        }
    }, [location.state]);
    const handleBackHome = ()=> {
        navigate('/search', { replace: true });
      }
    useEffect(() => {
        const handleAllData = async () => {
            console.log("Subject ID to fetch data for:", subject_id);
            
            if (subject_id !== -1) {  
                try {
                    const response = await axios.post(
                        'http://127.0.0.1:8000/teacher_subject/get_all_teachers_of_subject',
                        { subject_id: subject_id },
                        {
                            headers: {
                                'Content-Type': 'application/json',
                                Accept: 'application/json',
                            },
                        }
                    );
                    console.log(response.data);
                    setData(response.data)
                } catch (error) {
                    console.log('Error fetching teachers:', error);
                }
            } else {
                console.log("Invalid subject ID:", subject_id);
            }
        };

        handleAllData();
    }, [subject_id]); 

    return (
        <>
         <div className='flex flex-row gap-5 items-center justify-center flex-wrap mt-20'>
            {data.length > 0 ? 
                     data.map((result, key) => (
                   
                            <TCard                         
                                key={key}
                                name={result.full_name}
                                Score={result.total_average_score}
                                comment={result.number_of_comments}
                                imageURL={result.teacher_pic}
                              
                            />
                        
                    ))
                    
                    : <main className="farmer-motion h-80 w-full flex flex-col justify-center items-center">
                    <h1 className="text-9xl font-extrabold text-white tracking-widest">404</h1>
                    <div className="bg-red-900 px-2 text-sm rounded rotate-12 absolute">
                        نتیجه‌ای یافت نشد
                    </div>
                    <button class="mt-5">
                      <a
                        className="relative inline-block text-sm font-medium text-red-900 group active:text-red-500 focus:outline-none focus:ring"
                      >
                        <span
                          className="absolute inset-0 transition-transform translate-x-0.5 translate-y-0.5 bg-red-900 group-hover:translate-y-0 group-hover:translate-x-0"
                        ></span>
                
                        <span className="relative block px-8 py-3 bg-[#1A2238] border border-current">
                          <button onClick={handleBackHome}>بازگشت به صفحه‌ی جستجو</button>
                        </span>
                      </a>
                    </button>
                </main>
}
            </div>
        </>
    );
};

export default SubjectTeachers;
