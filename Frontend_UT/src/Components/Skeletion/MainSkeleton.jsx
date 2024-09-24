import React from 'react';
import Skeleton, { SkeletonTheme } from 'react-loading-skeleton';
import 'react-loading-skeleton/dist/skeleton.css';

const CardSkeleton = () => {
  return (
    <SkeletonTheme baseColor="#202020" highlightColor="#444">
      <div className="w-full min-h-screen text-white flex flex-col items-center justify-center p-4 pt-20 animate-pulse">
        <div>
          <main className="flex flex-col gap-4 w-full max-w-full mt-6 sm:py-5 md:py-22 lg:py-22 xl:py-18">
            {/* First Section Skeleton */}
            <div className="flex flex-col-reverse lg:flex-row items-center" dir="rtl">
              <div className="lg:w-1/2 animate-pulse">
                <Skeleton height={400} width={400} />
              </div>
              <div className="flex flex-col gap-2 items-start lg:w-1/2 p-4 text-center lg:text-right">
                <Skeleton width={400} height={60} />
                <Skeleton width={500} count={3} />
                <Skeleton width={350} height={50} style={{ marginTop: '20px' }} />
                <Skeleton width={250} height={50} />
              </div>
            </div>

            {/* Second Section Skeleton */}
            <div className="flex flex-col-reverse lg:flex-row lg:gap-4 items-center">
              <div className="lg:w-1/2 pb-4 animate-pulse">
                <Skeleton height={450} width={450} />
              </div>
              <div className="lg:w-1/2 pb-4">
                <Skeleton width={400} height={70} />
                <Skeleton width={300} height={60} />
              </div>
            </div>

            {/* Third Section Skeleton */}
            <div className="flex flex-col-reverse lg:flex-row items-center" dir="rtl">
              <div className="lg:w-1/2 animate-pulse">
                <Skeleton height={500} width={500} />
              </div>
              <div className="flex flex-col gap-2 items-start lg:w-1/2 p-4 text-center lg:text-right">
                <Skeleton width={400} height={80} />
                <Skeleton width={600} count={3} />
              </div>
            </div>
          </main>
        </div>
      </div>
    </SkeletonTheme>
  );
};

export default CardSkeleton;
