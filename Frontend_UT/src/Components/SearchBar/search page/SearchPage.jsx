import React, { useState, useEffect } from 'react';
import { AiOutlineSearch } from 'react-icons/ai';
import { useLocation } from 'react-router-dom';
import SwitchSearch from '../swichSearch';
import Searchbar from './Searchbar';
import ReviewCard from './Cards/TeacherCard';
import UniCards from './Cards/UniCards';
import SubjectCards from './Cards/SubjectCards';
import { useNavigate } from 'react-router-dom';
import Error404 from '../../Error/Error404';
import Back from '../../BackButton/Back';
import SkeletonReviewCard from '../../Skeletion/CardSkeletion';
import UniCardSkeleton from '../../Skeletion/unicardSkeleton';

const SearchPage = () => {
    const navigate = useNavigate();
    const location = useLocation(); 
    const [searchAsk, setSearchAsk] = useState(0);
    const [searchAsk2, setSearchAsk2] = useState(0);
    const [searchResult, setSearchResult] = useState([]);
    const [searchInput, setSearchInput] = useState('');
    const [error,setError]=useState(false)
    const [isLoading, setIsLoading] = useState(true);

 

    useEffect(() => {
        if (location.state) {
            if (location.state.searchAsk) {
                setSearchAsk(location.state.searchAsk);
            }
            if (location.state.searchInput) {
                setSearchInput(location.state.searchInput);
            }
        }
    }, [location.state]);

    useEffect(() => {
        Clear();
    }, [searchAsk]);

    const Clear = () => {
        setSearchResult([]);
       
    };


    return (
        <>
            <Searchbar 
                searchAsk={searchAsk} 
                searchAsk2={searchAsk2} 
                searchInput={searchInput} 
                setSearchInput={setSearchInput} 
                setSearchResult={setSearchResult} 
                setError={setError}
                setIsLoading={setIsLoading}
            />
          
            <div dir="rtl" className="w-full flex items-center justify-center m-auto mt-11">
                <SwitchSearch setSearchAsk={setSearchAsk} searchAsk={searchAsk} setSearchAsk2={setSearchAsk2}   />
            </div>

       {searchAsk === 1 && (
        <div className='flex flex-row gap-5 items-center justify-center flex-wrap'>
          {isLoading ? (
           <SkeletonReviewCard cards={8} />
          ) : searchResult.length > 0 ? (
            searchResult.map((result, key) => 
              result.teacher && (
                <ReviewCard                         
                  key={key}
                  id={result.teacher.id}
                  name={result.teacher.full_name}
                  Score={result.teacher.total_average_score}
                  teachingScore={result.teacher.average_teaching_score}
                  behaviorScore={result.teacher.average_behaviour_score}
                  gradingScore={result.teacher.average_grading_score}
                  comment={result.teacher.number_of_comments}
                  imageURL={result.teacher.teacher_pic}
                  subs={result.subjects}
                  unis={result.unis}
                />
              )
            )
          ) : error ? (
         
            <Error404 />
          ) : null}
        </div>
      )}

            {searchAsk === 2 && (
                <div className='flex flex-row gap-5 items-center justify-center flex-wrap'>
                    { isLoading ? (
                        <UniCardSkeleton cards={1} />
                       ) : searchResult.length > 0 ?
                        searchResult.map((result, key) => (
                            <UniCards                         
                                key={key}
                                name={result.name}
                                id={result.id}
                            />
                        )) : error ? <Error404/> :null
                    }
                </div>
            )}

            {searchAsk === 3 && (
                <div className='flex flex-row gap-5 items-center justify-center flex-wrap'>
                    {
                    isLoading ? (
                        <UniCardSkeleton cards={1} />
                       ) : searchResult.length > 0 ?
                        searchResult.map((result, key) => (
                            <SubjectCards                         
                                key={key}
                                name={result.name}
                                id={result.id}
                            />
                        )) : error ? <Error404/> :null
                    }
                </div>
            )}
            <Back/>
           
        </>
    );
};

export default SearchPage;
