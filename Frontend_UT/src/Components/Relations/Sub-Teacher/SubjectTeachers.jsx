import React, { useState, useEffect } from 'react';
import { useNavigate, useLocation } from 'react-router-dom';
import axios from 'axios';
import TCard from './TCard';
import Error404 from '../../Error/Error404';
import ReviewCard from '../../SearchBar/search page/Cards/TeacherCard';
import Back from '../../BackButton/Back';
import Skeleton from 'react-loading-skeleton';
import 'react-loading-skeleton/dist/skeleton.css';
import SkeletonReviewCard from '../../Skeletion/CardSkeletion';

const SubjectTeachers = () => {
    const navigate = useNavigate();
    const location = useLocation();
    const [subject_id, setSubjectId] = useState(-1);
    const [data, setData] = useState([]);
    const [title, setTitle] = useState('برترین اساتید');
    const [bestTeachers, setBestTeachers] = useState([]);
    const [isDataLoading, setIsDataLoading] = useState(true);
    useEffect(() => {
        if (location.state && location.state.subject_id) {
            setSubjectId(location.state.subject_id);
        }
    }, [location.state]);

    useEffect(() => {
        const fetchAllData = async () => {
            if (subject_id === -1) {
                setIsDataLoading(false)
            }
            if (subject_id !== -1) {
                setIsDataLoading(true);
                try {
                    const [teachersResponse, bestTeachersResponse] = await Promise.all([
                        axios.post(
                            'http://127.0.0.1:8000/teacher_subject/get_all_teachers_of_subject',
                            { subject_id },
                            {
                                headers: {
                                    'Content-Type': 'application/json',
                                    Accept: 'application/json',
                                },
                            }
                        ),
                        axios.post(
                            'http://127.0.0.1:8000/subject/get_best_teachers_of_subject',
                            { subject_id, limit: 12 },
                            {
                                headers: {
                                    'Content-Type': 'application/json',
                                    Accept: 'application/json',
                                },
                            }
                        ),
                    ]);
                    setData(teachersResponse.data);
                    setBestTeachers(bestTeachersResponse.data);
                } catch (error) {
                    console.log('Error fetching teachers:', error);
                   
                } finally {
                    setIsDataLoading(false);
                }
            }
        };

        fetchAllData();
    }, [subject_id]);

    return (
        <div className="flex flex-col gap-5 pt-11 bg-background-light dark:bg-background-dark">
            <div>
                <h1 className="flex items-center justify-center font-iran font-bold break-normal text-text-gray dark:text-text-light px-2 text-xl mt-10 lg:mt-0 md:text-2xl">
                    {title || <Skeleton />}
                </h1>
                <Back />
                <hr className="bg-gray-300 my-6 w-10/12 m-auto" />
            </div>
            <div className='flex flex-row gap-5 items-center justify-center flex-wrap mt-1 mb-20'>
                {isDataLoading ? (
                    <SkeletonReviewCard cards={3} />
                ) : bestTeachers.length > 0 ? 
                    bestTeachers.map((result, key) => (
                        result.teacher && (
                            <ReviewCard                         
                                key={key}
                                id={result.teacher.id}
                                name={result.teacher.full_name}
                                Score={Number(result.total_average_score ?? 0)}
                                comment={result.teacher.number_of_comments}
                                imageURL={result.teacher.teacher_pic}
                                subs={result.subjects}
                                unis={result.unis}
                            />
                        )
                    )) : <Error404 />
                }
            </div>

            <div>
                <h1 className="flex items-center justify-center font-iran font-bold break-normal text-text-gray px-2 text-xl mt-20 lg:mt-0 md:text-2xl">
                    تمام اساتید این درس
                </h1>
                <hr className="bg-gray-300 my-6 w-10/12 m-auto" />
            </div>
            <div className='flex flex-row gap-5 items-center justify-center flex-wrap mt-1 mb-20'>
                {isDataLoading ? (
                    <SkeletonReviewCard cards={3} />
                ) : data.length > 0 ? 
                    data.map((result, key) => (
                        <TCard                         
                            key={key}
                            name={result.full_name}
                            Score={Number(result.total_average_score ?? 0)}
                            comment={result.number_of_comments}
                            imageURL={result.teacher_pic}
                        />
                    )) : <Error404 />
                }
            </div>
        </div>
    );
};

export default SubjectTeachers;
