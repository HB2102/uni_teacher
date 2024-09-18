import React from 'react';
import Skeleton , { SkeletonTheme }from 'react-loading-skeleton';
import 'react-loading-skeleton/dist/skeleton.css';

const SkeletonReviewCard = ({cards}) => {
  return (
    Array(cards) // Adjust the number of skeleton cards based on how many you want to show while loading
    .fill(0)
    .map((_, index) =>  <article key={index} dir='rtl' className="farmer-motion p-5 bg-white dark:bg-gray-800 rounded-lg shadow-md w-10/12 sm:w-[48%] md:w-[48%] lg:w-1/4 xl:w-1/5 mt-9">
    <div dir='rtl' className="flex items-center mb-4">
      <Skeleton circle={true} height={40} width={40} className="ml-4" />
      <div className="font-medium dark:text-white">
        <h2>
          <Skeleton width={120} />
        </h2>
      </div>
    </div>

    <p className="mb-2 mt-4 text-gray-500 dark:text-gray-400">
      <Skeleton count={2} />
    </p>
    <p className="mb-3 text-gray-500 dark:text-gray-400">

      <Skeleton count={2} />
    </p>

    <aside dir='ltr'>
     
      <button className="mt-1 ml-1 text-xs text-gray-500 dark:text-gray-400">
        <Skeleton width={100} />
      </button>
      <div className="flex items-center mt-3">
        <Skeleton width={100} height={30} className="px-3 py-2" />
        <Skeleton width={120} height={30} className="ml-4 pl-4" />
      </div>
    </aside>
  </article>
   
  ));
};

export default SkeletonReviewCard;
