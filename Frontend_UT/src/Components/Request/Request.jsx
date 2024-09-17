import React, { useState, useEffect } from 'react';
import { IoMdArrowDropdown } from "react-icons/io";
import "./request.css";
import DefaultRequest from './DefultRequest';
import Footer from '../Footer/Footer';
import AddTeacher from './AddTeacher';
import AddUni from './AddUni';
import { useNavigate } from 'react-router-dom';
import AddSubject from './AddSubject';
import Back from '../BackButton/Back';

const Request = () => {
  const navigate = useNavigate();
  const [ask, setAsk] = useState(0);
  const [menuContentVisible, setMenuContentVisible] = useState(false);

  const handleMenuToggle = () => {
    setMenuContentVisible(!menuContentVisible);
  };
  const handleBackHome = ()=> {
    navigate("/");
  }
  const handleClickDefult = () => setAsk(0);
  const handleAddTeacher = () => setAsk(1);
  const handleAddUni = () => setAsk(2);
  const handleAddSubject = () => setAsk(3);

  const renderContent = () => {
    switch (ask) {
      case 3:
        return (<AddSubject />);
      case 1:
        return (<AddTeacher />);
      case 2:
        return (<AddUni />);
      default:
        return <DefaultRequest />;
    }
  };

  return (
    <div dir="rtl" className="bg-background-light dark:bg-background-dark dark:text-text-light tracking-wider leading-normal rtl">
      <div className="container w-full flex flex-wrap mx-auto px-2 pt-8 lg:pt-10 ">
        <div className="w-full lg:w-1/5 px-6 text-xl text-gray-800 leading-normal">
          <div className="block lg:hidden sticky inset-0">
            <button
              id="menu-toggle"
              onClick={handleMenuToggle}
              className="flex w-full justify-end px-3 py-3 bg-white lg:bg-transparent border rounded border-gray-600 hover:border-icons-dark appearance-none focus:outline-none"
            >
              <IoMdArrowDropdown className="fill-current h-3 float-right" />
            </button>
          </div>

          <div
            className={`w-full sticky inset-6 max-h-64 lg:h-auto overflow-x-hidden overflow-y-auto lg:overflow-y-hidden lg:block mt-0 my-2 lg:my-0 border border-gray-400 lg:border-transparent bg-white shadow lg:shadow-none lg:bg-transparent z-20 ${menuContentVisible ? '' : 'hidden'}`}
            style={{ top: '6em' }}
            id="menu-content"
          >
            <ul className="list-reset py-2 md:py-0">
              <li 
                onClick={handleClickDefult} 
                className={`py-1 md:my-2 hover:bg-teal-50 lg:hover:bg-transparent border-r-4 ${ask === 0 ? 'border-teal-600 font-bold' : 'border-transparent'}`}
              >
                <p
                  
                  className="block pr-4 align-middle text-gray-700 no-underline hover:text-gray-950"
                >
                  <span className="pb-1 md:pb-0 text-sm">ثبت درخواست</span>
                </p>
              </li>
              <li 
                onClick={handleAddTeacher} 
                className={`py-1 md:my-2 hover:bg-teal-50 lg:hover:bg-transparent border-r-4 ${ask === 1 ? 'border-teal-600 font-bold' : 'border-transparent'}`}
              >
                <p
                  className="block pr-4 align-middle text-gray-700 no-underline hover:text-gray-950"
                >
                  <span className="pb-1 md:pb-0 text-sm">افزودن استاد</span>
                </p>
              </li>
              <li 
                onClick={handleAddUni} 
                className={`py-1 md:my-2 hover:bg-teal-50 lg:hover:bg-transparent border-r-4 ${ask === 2 ? 'border-teal-600 font-bold' : 'border-transparent'}`}
              >
                <p
                  className="block pr-4 align-middle text-gray-700 no-underline hover:text-gray-950"
                >
                  <span className="pb-1 md:pb-0 text-sm">افزودن دانشگاه</span>
                </p>
              </li>
              <li 
                onClick={handleAddSubject} 
                className={`py-1 md:my-2 hover:bg-teal-50 lg:hover:bg-transparent border-r-4 ${ask === 3 ? 'border-teal-600 font-bold' : 'border-transparent'}`}
              >
                <p
                  className="block pr-4 align-middle text-gray-700 no-underline hover:text-gray-950"
                >
                  <span className="pb-1 md:pb-0 text-sm">افزودن درس</span>
                </p>
              </li>
            </ul>
          </div>
        </div>

        {/* Section container */}
        <section className="w-full lg:w-4/5">
          <h1 className="flex items-center font-iran font-bold break-normal text-text-gray px-2 text-xl mt-12 lg:mt-0 md:text-2xl ">
            پیشنهادات خود را با ما درمیان بگذارید
          </h1>

          {/* Divider */}
          <hr className="bg-gray-300 my-12" />
          {renderContent()}
        </section>
        <div onClick={handleBackHome} className="w-full lg:w-4/5 lg:mr-auto text-base md:text-sm text-gray-600 px-4 py-5"> {/* Changed margin from left to right */}
          <span className="text-base text-teal-600 font-bold">&lt;</span>{' '}
          <a  className="text-base md:text-sm text-teal-600 font-bold no-underline hover:underline">
            بازگشت به صفحه‌ی اصلی
          </a>
        </div>
      </div>
      <div dir='ltr' className="mb-3 w-4/5 m-auto">
        <Footer />
      </div>
    </div>
  );
};

export default Request;
