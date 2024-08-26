import React, { useState } from "react";
import "./SignIn.css";
import { motion } from "framer-motion";
import { FaUser, FaLock } from "react-icons/fa";
import { GrFormNextLink } from "react-icons/gr";

const Signin = () => {
  const [showComponent, setshowComponent] = useState("Text");

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
            <form className="login-box" action="">
              <div className="flex flex-row justify-between">
                <h1>ورود </h1>
                <GrFormNextLink className="text-3xl" onClick={handleShowText}/>
              </div>

              <div className="input-box">
                <input type="text" required />
                <label>Username</label>
                <FaUser />
              </div>
              <div className="input-box">
                <input type="password" required />
                <label>Password</label>
                <FaLock />
              </div>

              <div className="remember-forgot">
                <label>
                  <input type="checkbox" />
                  Remember me
                </label>
                <a href="">Forgot password?</a>
              </div>

              <button className="button bg-teal-600" type="submit">
                Login
              </button>

              <div className="register-link">
                Don't have an account?{" "}
                <button
                  className="hover:text-teal-400 transition-all duration-300 hover:underline  after:h-0.5 after:bg-teal-400 after:transition-all after:duration-300 button p-0 pl-1"
                  onClick={handleShowRegister}
                >
                  Register
                </button>
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
              <form className="login-box" action="">
                <div className="flex flex-row justify-between">
                  <h1>ثبت نام</h1>
                  <GrFormNextLink className="text-3xl" onClick={handleShowText} />
                </div>

                <div className="input-box">
                  <input type="text" required />
                  <label>Username</label>
                  <FaUser />
                </div>

                <div className="remember-forgot">
                  <label>
                    <input type="checkbox" />
                    Remember me
                  </label>
                  <a href="">Forgot password?</a>
                </div>

                <button className="button bg-teal-600" type="submit">
                  Login
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
                className="bg-teal-500 text-xl px-4 py-2 rounded-full text-white hover:bg-teal-600 align-middle"
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
