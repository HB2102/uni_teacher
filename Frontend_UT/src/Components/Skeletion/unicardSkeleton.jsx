import React from 'react';
import Skeleton from 'react-loading-skeleton';
import 'react-loading-skeleton/dist/skeleton.css';

const UniCardSkeleton = ({cards}) => {
  return (
    Array(cards) // Adjust the number of skeleton cards based on how many you want to show while loading
    .fill(0)
    .map((_, index) => 
    <article key={index} dir='rtl' className="p-5 bg-white dark:bg-gray-800 rounded-lg shadow-md w-10/12 sm:w-[48%] md:w-[48%] lg:w-1/4 xl:w-1/5 mt-9">
      <div dir='rtl' className="flex items-center mb-4">
        <Skeleton circle={true} height={40} width={40} className="ml-4" />
        <div className="flex flex-col space-y-2 w-full">
          <Skeleton width={`75%`} height={20} />
        </div>
      </div>

      <aside dir='ltr'>
        <div className="flex items-center mt-3 space-x-4">
          <Skeleton width={80} height={30} className="rounded-lg" />
          <Skeleton width={100} height={30} />
        </div>
      </aside>
    </article>
  ))
};

export default UniCardSkeleton;
