import React from "react";
import "./SignIn.css";
import { motion } from "framer-motion";
import { FaUser, FaLock } from "react-icons/fa";

const Signin = () => {
  return (
    <div className="">
      <div className="flexCenter paddings innerWidth hero-container">
        {/* left side */}
        <div className="flexColStart ">
          <motion.div
            initial={{ x: "-7rem", opacity: 0 }}
            animate={{ x: 0, opacity: 1 }}
            transition={{
              duration: 2,
              type: "spring",
            }}
          >
           
            <form className="login-box" action="">
              <h1>Login</h1>
              <div className="input-box">
                <input type="text" required />
                <label for="">Username</label>
                <FaUser />
              </div>
              <div className="input-box">
                <input type="password" required />
                <label for="">Password</label>
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
                Don't have an account? <a href="">Register</a>
              </div>
            </form>
          </motion.div>
        </div>

      
      </div>
    </div>
  );
};

export default Signin;
