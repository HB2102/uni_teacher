import React, { useRef, useState, useEffect } from 'react';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';
import Swal from "sweetalert2";  

const OTPVerification = ({ signInData, setSignInData }) => {
  const navigate = useNavigate();
  const inputsRef = useRef([]);
  const [verificationCode, setVerificationCode] = useState('');

  const handleKeyDown = (e, index) => {
    const input = e.target;

    
    if (!/^[0-9]{1}$/.test(e.key) && e.key !== 'Backspace' && e.key !== 'Delete' && e.key !== 'Tab') {
      e.preventDefault();
    }

    if (e.key === 'Delete' || e.key === 'Backspace') {

      if (input.value !== '') {
        inputsRef.current[index].value = '';
        updateVerificationCode();
      } else {
        if (index > 0 && e.key === 'Backspace') {
          inputsRef.current[index - 1].focus();
        }
      }
    }
  };

  const handleInput = (e, index) => {
    const input = e.target;
    if (input.value && index < inputsRef.current.length - 1) {
      inputsRef.current[index + 1].focus();
    }
    updateVerificationCode();
  };

  const handleFocus = (e) => {
    e.target.select();
  };

  const handlePaste = (e) => {
    e.preventDefault();
    const text = e.clipboardData.getData('text');
    if (!new RegExp(`^[0-9]{${inputsRef.current.length}}$`).test(text)) {
      return;
    }

    const digits = text.split('');
    digits.forEach((digit, index) => {
      inputsRef.current[index].value = digit;
    });
    updateVerificationCode();
    inputsRef.current[inputsRef.current.length - 1].focus();
  };

  // Function to update the verification code in the state
  const updateVerificationCode = () => {
    const code = inputsRef.current.map(input => input.value).join('');
    setVerificationCode(code);
  };
  const handleSubmit = async(e) => {
    e.preventDefault();
    console.log('Submitted Verification Code:', verificationCode);
    try {
        const response = await axios.post('http://127.0.0.1:8000/user/user_forget_password_check', {
          username: signInData.username ,
          code : verificationCode
        }, {
          headers: {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
          },
        });
        console.log(response);

        // Handle success
        if (response.status === 200) {
          

            try {
                const response = await axios.post('http://127.0.0.1:8000/token', signInData, {
                  headers: {
                    'Content-Type': 'multipart/form-data'
                  }
                });
          
                if (response.status === 200) { 
                  localStorage.setItem('Token', response.data.access_token );
                  navigate('/user-Panel');
          
                  Swal.fire({
                    position: "top-end",
                    title: 'خوش آمدید',
                    showConfirmButton: false,
                    timerProgressBar: true,
                    timer: 3000,
                    background: '#ffffff', 
                    width: '400px',
                    padding: '0.5em', 
                    customClass: {
                        title: 'small-alert-title', 
                    },
                    didOpen: () => {
                        const progressBar = Swal.getTimerProgressBar();
                        progressBar.style.backgroundColor = '#00ff00'; 
                        progressBar.style.height = '3px';
                        progressBar.style.width = '100%'; 
                    }
                })
          
                  setSignUpData({
                    username: '',
                    password: '',
                  });
                }
          
              } catch (error) {
                console.error('Error creating user:', error);
                Swal.fire({
                  position: "top-end",
                  title: "Error!",
                  text: "There was a problem creating the user.",
                  icon: "error",
                  timer: 3000,
                  timerProgressBar: true, 
                  showConfirmButton: true, 
                });
              }
        }
      } catch (error) {
        console.log('Error during verification', error);
        Swal.fire('Error', 'Request failed. Please try again.', 'error');
      }
   
  };

  

  return (
    <div dir="ltr" className="max-w-md mx-auto text-center  rounded-xl shadow">
      <header className="mb-8">
        <h1 className="text-2xl font-bold mb-1">تایید شماره تلفن</h1>
        <p className="text-[15px] text-slate-500">
          کد تأیید 4 رقمی را وارد کنید
        </p>
      </header>
      <form onSubmit={handleSubmit}>
        <div className="flex items-center justify-center gap-3">
          {[...Array(6)].map((_, index) => (
            <input
              key={index}
              type="text"
              maxLength="1"
              ref={(el) => (inputsRef.current[index] = el)}
              className="w-14 h-14 text-center text-2xl font-extrabold text-slate-900 bg-slate-100 border border-transparent hover:border-slate-200 appearance-none rounded p-4 outline-none focus:bg-white focus:border-indigo-400 focus:ring-2 focus:ring-indigo-100"
              onKeyDown={(e) => handleKeyDown(e, index)}
              onInput={(e) => handleInput(e, index)}
              onFocus={handleFocus}
              onPaste={handlePaste}
            />
          ))}
        </div>

        <div className="max-w-[260px] mx-auto mt-4">
          <button
            type="submit"
            className="w-full inline-flex justify-center whitespace-nowrap rounded-lg bg-indigo-500 px-3.5 py-2.5 text-sm font-medium text-white shadow-sm shadow-indigo-950/10 hover:bg-indigo-600 focus:outline-none focus:ring focus:ring-indigo-300 focus-visible:outline-none focus-visible:ring focus-visible:ring-indigo-300 transition-colors duration-150"
          >
            Verify Account
          </button>
        </div>
      </form>

      <div className="text-sm text-slate-500 mt-4">
        Didn't receive code?{' '}
        <a className="font-medium text-indigo-500 hover:text-indigo-600" href="#0">
          Resend
        </a>
      </div>
    </div>
  );
};

export default OTPVerification;
