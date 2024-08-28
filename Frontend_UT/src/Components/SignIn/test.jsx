import React, { useEffect, useState } from "react";
import './SignIn.css';

const Window= () => {
 
 const [isModalOpen, setIsModalOpen] = useState(false);

 const toggleModal = () => {
   setIsModalOpen(!isModalOpen);
  
 };

 return (
   <div className="relative">
     <button
       onClick={toggleModal}
       className="px-4 py-2 bg-red-500 text-white rounded"
     >
       کلیک نکن
     </button>

    
     {isModalOpen && <Modal toggleModal={toggleModal} />}
   </div>
 );
}

function Modal({ toggleModal }) {
 return (
   <>
    
     <div
       className="fixed inset-0 bg-black bg-opacity-50"
       onClick={toggleModal}
     ></div>
     <div className="fixed inset-0 flex items-center justify-center">
       <div className="bg-white p-6 rounded-lg shadow-lg relative">
         <button
           onClick={toggleModal}
           className="absolute top-2 right-2 text-gray-500"
         >
           &times;
         </button>
         <h2 className="text-lg font-semibold mb-4">اسکل و تورو قرآن</h2>
         <p className="mb-4">This is the modal content.</p>
       </div>
     </div>
   </>
 );
};

export default Window;
