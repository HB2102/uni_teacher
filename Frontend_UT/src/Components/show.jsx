import React, { useState, useEffect } from 'react';
import { IoMdArrowDropdown } from "react-icons/io";
const Request = () => {
  const [userMenuVisible, setUserMenuVisible] = useState(false);
  const [menuContentVisible, setMenuContentVisible] = useState(false);

  useEffect(() => {
    const handleDocumentClick = (e) => {
      // User Menu
      if (!e.target.closest('#userMenu') && !e.target.closest('#userButton')) {
        setUserMenuVisible(false);
      }

      // Help Menu
      if (!e.target.closest('#menu-content') && !e.target.closest('#menu-toggle')) {
        setMenuContentVisible(false);
      }
    };

    document.addEventListener('click', handleDocumentClick);

    return () => {
      document.removeEventListener('click', handleDocumentClick);
    };
  }, []);

  useEffect(() => {
    const handleScrollSpy = () => {
      const topMenu = document.getElementById('menu-content');
      const topMenuHeight = topMenu ? topMenu.offsetHeight + 175 : 0;
      const menuItems = topMenu ? topMenu.querySelectorAll('a') : [];
      const scrollItems = Array.from(menuItems).map((menuItem) => {
        const item = document.querySelector(menuItem.getAttribute('href'));
        return item ? item : null;
      });

      let lastId = '';

      const handleScroll = () => {
        const fromTop = window.scrollY + topMenuHeight;
        let cur = scrollItems.filter((item) => item && item.offsetTop < fromTop);
        cur = cur[cur.length - 1];
        const id = cur ? cur.id : '';

        if (lastId !== id) {
          lastId = id;
          menuItems.forEach((menuItem) => {
            const parent = menuItem.parentNode;
            parent.classList.remove('font-bold', 'border-yellow-600');
            if (menuItem.getAttribute('href') === `#${id}`) {
              parent.classList.add('font-bold', 'border-yellow-600');
            }
          });
        }
      };

      window.addEventListener('scroll', handleScroll);
      return () => {
        window.removeEventListener('scroll', handleScroll);
      };
    };

    handleScrollSpy();
  }, []);

  const handleMenuToggle = () => {
    setMenuContentVisible(!menuContentVisible);
  };

  return (
    <div className="bg-background-light dark:bg-background-dark dark:text-text-light text-gray-900 tracking-wider leading-normal rtl">


      <div className="container w-full flex flex-wrap mx-auto px-2 pt-8 lg:pt-16 ">
        <div className="w-full lg:w-1/5 px-6 text-xl text-gray-800 leading-normal">
          <p className="text-base font-bold py-2 lg:pb-6 text-gray-700">Menu</p>
          <div className="block lg:hidden sticky inset-0">
            <button
              id="menu-toggle"
              onClick={handleMenuToggle}
              className="flex w-full justify-end px-3 py-3 bg-white lg:bg-transparent border rounded border-gray-600 hover:border-yellow-600 appearance-none focus:outline-none"
            >
              <IoMdArrowDropdown  className="fill-current h-3 float-right"/>
            </button>
          </div>

          <div
            className={`w-full sticky inset-6 max-h-64 lg:h-auto overflow-x-hidden overflow-y-auto lg:overflow-y-hidden lg:block mt-0 my-2 lg:my-0 border border-gray-400 lg:border-transparent bg-white shadow lg:shadow-none lg:bg-transparent z-20 ${
              menuContentVisible ? '' : 'hidden'
            }`}
            style={{top:'6em'}}
            id="menu-content"
          >
            <ul className="list-reset py-2 md:py-0">
              <li className="py-1 md:my-2 hover:bg-yellow-100 lg:hover:bg-transparent border-l-4 border-transparent font-bold border-yellow-600">
                <a
                  href="#section1"
                  className="block pl-4 align-middle text-gray-700 no-underline hover:text-yellow-600"
                >
                  <span className="pb-1 md:pb-0 text-sm">Section 1</span>
                </a>
              </li>
              <li className="py-1 md:my-2 hover:bg-yellow-100 lg:hover:bg-transparent border-l-4 border-transparent">
                <a
                  href="#section2"
                  className="block pl-4 align-middle text-gray-700 no-underline hover:text-yellow-600"
                >
                  <span className="pb-1 md:pb-0 text-sm">Section 2</span>
                </a>
              </li>
              <li className="py-1 md:my-2 hover:bg-yellow-100 lg:hover:bg-transparent border-l-4 border-transparent">
                <a
                  href="#section3"
                  className="block pl-4 align-middle text-gray-700 no-underline hover:text-yellow-600"
                >
                  <span className="pb-1 md:pb-0 text-sm">Section 3</span>
                </a>
              </li>
              <li className="py-1 md:my-2 hover:bg-yellow-100 lg:hover:bg-transparent border-l-4 border-transparent">
                <a
                  href="#section4"
                  className="block pl-4 align-middle text-gray-700 no-underline hover:text-yellow-600"
                >
                  <span className="pb-1 md:pb-0 text-sm">Section 4</span>
                </a>
              </li>
              {/* <li className="py-1 md:my-2 hover:bg-yellow-100 lg:hover:bg-transparent border-l-4 border-transparent">
                <a
                  href="#section5"
                  className="block pl-4 align-middle text-gray-700 no-underline hover:text-yellow-600"
                >
                  <span className="pb-1 md:pb-0 text-sm">Section 5</span>
                </a>
              </li> */}
            </ul>
          </div>
        </div>

        {/* Section container */}
        <section className="w-full lg:w-4/5">
          {/* Title */}
          <h1 className="flex items-center font-iran font-bold break-normal text-text-gray px-2 text-xl mt-12 lg:mt-0 md:text-2xl ">
            پیشنهادات خود را با ما درمیان بگذارید
          </h1>

          {/* Divider */}
          <hr className="bg-gray-300 my-12" />

          {/* Section 1 */}
          {/* <h2 id="section1" className="font-iran font-bold break-normal text-gray-700 px-2 pb-8 text-xl">
            Section 1
          </h2>
          <div className="p-8 mt-6 lg:mt-0 leading-normal rounded shadow bg-white">
            <li>
              Using the CDN version of{' '}
              <a
                className="underline text-yellow-600"
                href="https://github.com/tailwindcss/custom-forms"
                target="_blank"
                rel="noopener noreferrer"
              >
                Tailwind Custom Forms
              </a>
            </li>
            <li>This template uses JavaScript for scrollspy</li>
          </div> */}

          {/* Divider */}
          {/* <hr className="bg-gray-300 my-12" /> */}

          {/* Section 2 */}
          <h2 id="section1" className=" font-iran font-bold break-normal text-text-gray px-2 pb-8 text-xl">
            ثبت درخواست
          </h2>
          <div className="p-8 mt-6 lg:mt-0 rounded shadow bg-white">
            <form>
              <div className="md:flex mb-6">
                <div className="md:w-1/3">
                  <label
                    className="block text-gray-600 font-bold md:text-left mb-3 md:mb-0 pr-4"
                    htmlFor="my-textfield"
                  >
                    Text Field
                  </label>
                </div>
                <div className="md:w-2/3 ">
                  <input
                    className="form-input block w-full focus:bg-white h-11 rounded-md"
                    id="my-textfield"
                    type="email"
                    value=""
                  />
                  <p className="py-2 text-sm text-gray-600">add notes about populating the field</p>
                </div>
              </div>

              {/* <div className="md:flex mb-6">
                <div className="md:w-1/3">
                  <label
                    className="block text-gray-600 font-bold md:text-left mb-3 md:mb-0 pr-4"
                    htmlFor="my-select"
                  >
                    Drop down field
                  </label>
                </div>
                <div className="md:w-2/3 h-11">
                  <select className="form-select block w-full focus:bg-white h-11 rounded-md" id="my-select">
                    <option value="Default">Default</option>
                    <option value="A">A</option>
                    <option value="B">B</option>
                    <option value="C">C</option>
                  </select>
                  <p className="py-2 text-sm text-gray-600">add notes about populating the field</p>
                </div>
              </div> */}

              <div className="md:flex mb-6">
                <div className="md:w-1/3">
                  <label
                    className="block text-gray-600 font-bold md:text-left mb-3 md:mb-0 pr-4"
                    htmlFor="my-textarea"
                  >
                    Text Area
                  </label>
                </div>
                <div className="md:w-2/3">
                  <textarea
                    className="form-textarea block w-full focus:bg-white rounded-md"
                    id="my-textarea"
                    rows="8"
                  ></textarea>
                  <p className="py-2 text-sm text-gray-600">add notes about populating the field</p>
                </div>
              </div>

              <div className="md:flex md:items-center">
                <div className="md:w-1/3"></div>
                <div className="md:w-2/3">
                  <button
                    className="shadow bg-yellow-700 hover:bg-yellow-500 focus:shadow-outline focus:outline-none text-white font-bold py-2 px-4 rounded"
                    type="button"
                  >
                    Save
                  </button>
                </div>
              </div>
            </form>
          </div>

          {/* Divider */}
          <hr className="bg-gray-300 my-12" />

          {/* Section 3 */}
          <h2 id="section3" className="font-iran font-bold break-normal text-gray-700 px-2 pb-8 text-xl">
            Section 3
          </h2>
          <div className="p-8 mt-6 lg:mt-0 rounded shadow bg-white">
            <form>
              <div className="md:flex mb-6">
                <div className="md:w-1/3">
                  <label
                    className="block text-gray-600 font-bold md:text-left mb-3 md:mb-0 pr-4"
                    htmlFor="my-multiselect"
                  >
                    Multi Select
                  </label>
                </div>
                <div className="md:w-2/3">
                  <select className="form-multiselect block w-full" multiple id="my-multiselect">
                    <option>Option 1</option>
                    <option>Option 2</option>
                    <option>Option 3</option>
                    <option>Option 4</option>
                    <option>Option 5</option>
                  </select>
                  <p className="py-2 text-sm text-gray-600">add notes about populating the field</p>
                </div>
              </div>

              <div className="md:flex md:items-center">
                <div className="md:w-1/3"></div>
                <div className="md:w-2/3">
                  <button
                    className="shadow bg-yellow-700 hover:bg-yellow-500 focus:shadow-outline focus:outline-none text-white font-bold py-2 px-4 rounded"
                    type="button"
                  >
                    Save
                  </button>
                </div>
              </div>
            </form>
          </div>

          {/* Divider */}
          <hr className="bg-gray-300 my-12" />

          {/* Section 4 */}
          <h2 id="section4" className="font-iran font-bold break-normal text-gray-700 px-2 pb-8 text-xl">
            Section 4
          </h2>
          <div className="p-8 mt-6 lg:mt-0 rounded shadow bg-white">
            <form>
              <div className="md:flex mb-6">
                <div className="md:w-1/3">
                  <label
                    className="block text-gray-600 font-bold md:text-left mb-3 md:mb-0 pr-4"
                    htmlFor="my-radio"
                  >
                    Radio Buttons
                  </label>
                </div>
                <div className="md:w-2/3">
                  <div className="mt-2">
                    <label className="inline-flex items-center">
                      <input type="radio" className="form-radio text-indigo-600" name="radioOption" value="A" />
                      <span className="ml-2">Radio A</span>
                    </label>
                    <label className="inline-flex items-center ml-6">
                      <input type="radio" className="form-radio" name="radioOption" value="B" />
                      <span className="ml-2">Radio B</span>
                    </label>
                  </div>
                  <p className="py-2 text-sm text-gray-600">add notes about populating the field</p>
                </div>
              </div>

              <div className="md:flex mb-6">
                <div className="md:w-1/3">
                  <label
                    className="block text-gray-600 font-bold md:text-left mb-3 md:mb-0 pr-4"
                    htmlFor="my-checkbox"
                  >
                    Checkboxes
                  </label>
                </div>
                <div className="md:w-2/3">
                  <div>
                    <label className="inline-flex items-center">
                      <input type="checkbox" className="form-checkbox text-indigo-600" checked />
                      <span className="ml-2">Option 1</span>
                    </label>
                  </div>
                  <div>
                    <label className="inline-flex items-center">
                      <input type="checkbox" className="form-checkbox text-green-500" checked />
                      <span className="ml-2">Option 2</span>
                    </label>
                  </div>
                  <div>
                    <label className="inline-flex items-center">
                      <input type="checkbox" className="form-checkbox text-pink-600" checked />
                      <span className="ml-2">Option 3</span>
                    </label>
                  </div>
                  <p className="py-2 text-sm text-gray-600">add notes about populating the field</p>
                </div>
              </div>

              <div className="md:flex md:items-center">
                <div className="md:w-1/3"></div>
                <div className="md:w-2/3">
                  <button
                    className="shadow bg-yellow-700 hover:bg-yellow-500 focus:shadow-outline focus:outline-none text-white font-bold py-2 px-4 rounded"
                    type="button"
                  >
                    Save
                  </button>
                </div>
              </div>
            </form>
          </div>

          {/* Divider */}
          <hr className="bg-gray-300 my-12" />

          {/* Section 5 */}
          <h2 id="section5" className="font-iran font-bold break-normal text-gray-700 px-2 pb-8 text-xl">
            Section 5
          </h2>
          <div className="p-8 mt-6 lg:mt-0 rounded shadow bg-white">
            <blockquote className="border-l-4 border-yellow-600 italic my-4 pl-8 md:pl-12">
              Final confirmation disclaimer message etc
            </blockquote>

            <div className="pt-8">
              <button
                className="shadow bg-yellow-700 hover:bg-yellow-500 focus:shadow-outline focus:outline-none text-white font-bold py-2 px-4 rounded mr-4"
                type="button"
              >
                Save
              </button>

              <button
                className="shadow bg-yellow-100 hover:bg-yellow-200 focus:shadow-outline focus:outline-none text-gray-700 font-bold py-2 px-4 rounded mr-4"
                type="button"
              >
                Additional Action
              </button>

              <button
                className="shadow bg-yellow-100 hover:bg-yellow-200 focus:shadow-outline focus:outline-none text-gray-700 font-bold py-2 px-4 rounded"
                type="button"
              >
                Additional Action
              </button>
            </div>
          </div>
        </section>
      </div>

      {/* Back link */}
      <div className="w-full lg:w-4/5 lg:ml-auto text-base md:text-sm text-gray-600 px-4 py-24 mb-12">
        <span className="text-base text-yellow-600 font-bold">&lt;</span>{' '}
        <a href="#" className="text-base md:text-sm text-yellow-600 font-bold no-underline hover:underline">
          Back link
        </a>
      </div>
    </div>
  );
};

export default Request;
