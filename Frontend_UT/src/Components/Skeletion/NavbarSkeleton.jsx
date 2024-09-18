import React from 'react';
import Skeleton  , { SkeletonTheme }from 'react-loading-skeleton';
import 'react-loading-skeleton/dist/skeleton.css';

const NavbarSkeleton = () => {
  return (
    <SkeletonTheme baseColor="#030712" highlightColor="#444">
    <div>
      <div>
        <header className="navbar flex justify-between items-center bg-teal-800 bg-opacity-25 w-full mt-6 mb-1 relative p-6 rounded-3xl">
          
          {/* DarkModeSwitch Placeholder */}
          <Skeleton circle={true} width={40} height={40} />

          {/* Icons Placeholder */}
          <div className="hidden md:flex items-center">
            <Skeleton circle={true} width={40} height={40} className="mr-3" />
            <Skeleton circle={true} width={40} height={40} className="mr-3" />
            <Skeleton circle={true} width={40} height={40} className="mr-3" />
          </div>

          {/* Menu Icon Placeholder for Mobile */}
          <div className="sm:hidden">
            <Skeleton width={24} height={24} />
          </div>

          {/* Navbar Items Skeleton */}
          <nav className="absolute sm:relative top-full left-0 w-full sm:w-auto sm:bg-transparent p-6 sm:p-0 z-10">
            <ul className="flex flex-col gap-3 sm:flex-row sm:space-x-4 items-center">
              <li>
                <Skeleton width={80} height={24} />
              </li>
              <li>
                <Skeleton width={80} height={24} />
              </li>
              <li>
                <Skeleton width={80} height={24} />
              </li>
              <li>
                <Skeleton width={80} height={24} />
              </li>
              <li>
                <Skeleton width={80} height={24} />
              </li>
            </ul>
          </nav>
        </header>
      </div>
    </div>
    </SkeletonTheme >
  );
};

export default NavbarSkeleton;
