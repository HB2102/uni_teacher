import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import { useLocation } from 'react-router-dom';
import axios from 'axios';
import ReviewCard from '../../SearchBar/search page/Cards/TeacherCard';
import TCard from './TCard';
import { Button } from 'bootstrap';
import Error404 from '../../Error/Error404';

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
                    
                    : <Error404/>
}
            </div>
        </>
    );
};

export default SubjectTeachers;
