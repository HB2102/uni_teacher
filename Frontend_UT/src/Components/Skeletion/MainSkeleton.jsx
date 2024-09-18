import React from 'react';
import Skeleton , { SkeletonTheme } from 'react-loading-skeleton';
import 'react-loading-skeleton/dist/skeleton.css';

const CardSkeleton = () => {
  return (
    <SkeletonTheme baseColor="#202020" highlightColor="#444">
    <div className="min-h-screen text-white flex flex-col items-center justify-center p-4 pt-20">
      <div>      
        <main className="flex flex-col gap-4 w-full max-w-full mt-6 sm:py-5 md:py-22 lg:py-22 xl:py-18">
          
        
          <div className="flex flex-col-reverse lg:flex-row lg:gap-10 items-center" dir="rtl">
            <div className="lg:w-1/2">
              <Skeleton height={350} width={350} />
             
            </div>
            <div className="flex flex-col gap-2 items-start lg:w-1/2 p-4 text-center lg:text-right">
              <Skeleton width={300} height={50} />
              <Skeleton width={400} count={3} />
              <Skeleton width={250} height={40} style={{ marginTop: '20px' }} />
              <Skeleton width={150} height={40} />
            </div>
          </div>

          {/* Second Section Skeleton */}
          <div className="flex flex-col-reverse lg:flex-row lg:gap-4 items-center">
            <div className="lg:w-1/2 pb-4">
              <Skeleton height={350} width={350} />
            
            </div>
            <div className="lg:w-1/2 pb-4">
              <Skeleton width={300} height={50} />
              <Skeleton width={200} height={40} />
            </div>
          </div>

          {/* Third Section Skeleton */}
          <div className="flex flex-col-reverse lg:flex-row items-center" dir="rtl">
            <div className="lg:w-1/2">
              <Skeleton height={350} width={350} />
            
            </div>
            <div className="flex flex-col gap-2 items-start lg:w-1/2 p-4 text-center lg:text-right">
              <Skeleton width={300} height={50} />
              <Skeleton width={400} count={3} />
            </div>
          </div>
        </main>
      </div>
    </div>
    </SkeletonTheme>
  );
};

export default CardSkeleton;
