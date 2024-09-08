import React, { useState } from "react";
import "./SignIn.css";
import { motion } from "framer-motion";
import { FaUser, FaLock } from "react-icons/fa";
import { GrFormNextLink } from "react-icons/gr";
import { FaPhoneFlip } from "react-icons/fa6";
import {BiLogoGmail } from "react-icons/bi";
import axios from 'axios';
import Swal from "sweetalert2";  
import { useNavigate } from 'react-router-dom';
const Signin = () => {
  const navigate = useNavigate();
  const [showComponent, setshowComponent] = useState("Text");
  const [signUpData, setSignUpData] = useState({
    username: '',
    password: '',
    phone_number:'',
    email:''
  });
  const [signInData, setSignInData] = useState({
    username: '',
    password: ''
  });
  const handleInputChange = (e) => {
    setSignUpData({
      ...signUpData,
      [e.target.name]: e.target.value
    });
    console.log(signUpData);
    
  };

  const handleInputChangeLogin = (e) => {
    setSignInData({
      ...signInData,
      [e.target.name]: e.target.value
    });
    console.log(signInData);
    
  };

  const handleSignUpSubmit = async () => {
    try {
      const response = await axios.post('http://127.0.0.1:8000/user/create_user', signUpData, {
        headers: {
          'Content-Type': 'application/json',
          'Accept': 'application/json',
        },
      });
  
      if (response.status === 201) { 
        navigate('/user-Panel');
        Swal.fire({
          position: "top-end",
          icon: "success",
          title: "اکانت شما با موفقیت ساخته شد",
          showConfirmButton: false,
          timerProgressBar: true,
          timer: 2000,
          background: '#ffffff',
          width: '400px',
          padding: '0.5em',
          customClass: {
              title: 'small-alert-title',
              icon: 'small-success-icon',  // Add a custom class for the icon
          },
          didOpen: () => {
              const progressBar = Swal.getTimerProgressBar();
              progressBar.style.backgroundColor = '#00ff00';
              progressBar.style.height = '3px';
              progressBar.style.width = '100%';
          }
      });
      

        setSignUpData({
          username: '',
          password: '',
          phone_number: '',
          email: ''
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
  };

  const handleSignInSubmit = async () => {
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
          timer: 2000,
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
        timer: 2000,
        timerProgressBar: true, 
        showConfirmButton: true, 
      });
    }
  };


  
  const handleShowLogin = () => {
    setshowComponent("Login");
    console.log(showComponent);
  };
  const handleShowRegister = () => {
    setshowComponent("Register");
    console.log(showComponent);
  };
  const handleShowText = () => {
    setshowComponent("Text");
    console.log(showComponent);
  };

  const renderContent = () => {
    switch (showComponent) {
      case "Login":
        return (
          <>
            <form className="login-box" action="" onSubmit={(e) => {
            e.preventDefault();
            handleSignInSubmit();
          }} >
              <div className="flex flex-row justify-between">
                <h1>ورود </h1>
                <GrFormNextLink className="text-3xl" onClick={handleShowText}/>
              </div>
              <div className="input-box ">
                  <input name="username" type="text" required value={signInData.username} onChange={handleInputChangeLogin}/>
                  <label>نام کاربری</label>
                  <FaUser />
                </div>
                <div className="input-box">
                  <input name="password" type="password" required value={signInData.password} onChange={handleInputChangeLogin} />
                  <label>رمز عبور</label>
                  <FaLock />
                </div>
              <div className="remember-forgot">
                  <label className="flex flex-row gap-2">
                  <input type="checkbox" />
                     فراموشم نکن
                    
                  </label>
                  <a href="">مزم یادم رفته</a>
                </div>
              <button className="button bg-teal-600" type="submit">
                Login
              </button>

              <div className="register-link">
              <button
                  className="hover:text-teal-400 transition-all duration-300 hover:underline  after:h-0.5 after:bg-teal-400 after:transition-all after:duration-300 button p-0 pr-1"
                  onClick={handleShowRegister}
                >
                  بسازید
                </button>
              {" "} حساب کاربری ندارید؟
          
              </div>
            </form>
          </>
        );
      case "Register":
        return (
          <>
            <motion.div
              initial={{ x: "-7rem", opacity: 0 }}
              animate={{ x: 0, opacity: 1 }}
              transition={{
                duration: 2,
                type: "spring",
              }}
            >
              <form className="login-box " action="" onSubmit={(e) => {
            e.preventDefault();
            handleSignUpSubmit();
          }}>
                <div className="flex flex-row justify-between">
                  <h1>ثبت نام</h1>
                  <GrFormNextLink className="text-3xl" onClick={handleShowText} />
                </div>

                <div className="input-box ">
                  <input name="username" type="text" required value={signUpData.username} onChange={handleInputChange}/>
                  <label>نام کاربری</label>
                  <FaUser />
                </div>
                <div className="input-box">
                  <input name="password" type="password" required value={signUpData.password} onChange={handleInputChange} />
                  <label>رمز عبور</label>
                  <FaLock />
                </div>
                <div className="input-box">
                  <input name="phone_number" type="text" required value={signUpData.phone_number} onChange={handleInputChange} />
                  <label>شماره موبایل</label>
                  <FaPhoneFlip />
                </div>
                <div className="input-box">
                  <input name="email" type="email" required value={signUpData.email} onChange={handleInputChange} />
                  <label>ایمیل</label>
                  <BiLogoGmail className="h-5 w-5"/>
                </div>

                <div className="remember-forgot">
                  <label className="flex flex-row gap-2">
                  <input type="checkbox" />
                     فراموشم نکن
                    
                  </label>
                  
                </div>

                <button className="button bg-teal-600" type="submit">
                  Sign up
                </button>

                <div className="register-link">
                  <button
                    className="hover:text-teal-400 transition-all duration-300 hover:underline  after:h-0.5 after:bg-teal-400 after:transition-all after:duration-300 button p-0 pr-1"
                    onClick={handleShowLogin}
                  >
                    ورود
                  </button>
                  حساب کاربری دارید؟
                </div>
              </form>
            </motion.div>
          </>
        );
      case "Text":
        return (
          <>
            <motion.div
              initial={{ x: "-7rem", opacity: 0 }}
              animate={{ x: 0, opacity: 1 }}
              transition={{
                duration: 2,
                type: "spring",
              }}
            >
            <div
              className="login-box space-y-2 text-right text-4xl lg:text-3xl md:text-3xl font-bold mb-6"
              dir="rtl"
            >
              <p className="flex items-center pb-5 leading-relaxed">
                عاهرذسصخدص
                <br />
                با داشتن حساب کاربری از امکانات بیشتری
                
                بهره‌مند شوید
              </p>
              <button
                onClick={handleShowLogin}
                className="bg-teal-500 text-xl px-4 py-2 rounded-full text-white hover:bg-teal-600"
                style={{ maxWidth: "150px" }}
              >
                ورود/ثبت نام
              </button>
            </div>
            </motion.div>
          </>
        );
      default:
        return null;
    }
  };

  return (
    <div className="flexCenter paddings innerWidth hero-container">
      {/* left side */}
      <div className="flexColStart">
        <motion.div
          initial={{ x: "-7rem", opacity: 0 }}
          animate={{ x: 0, opacity: 1 }}
          transition={{
            duration: 2,
            type: "spring",
          }}
        >
          {renderContent()}
        </motion.div>
      </div>
    </div>
  );
};

export default Signin;
