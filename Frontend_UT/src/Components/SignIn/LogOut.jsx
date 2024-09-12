import React, { useState } from 'react';
import Cookies from 'js-cookie';

const LogOut = ({ onLogOut }) => {
    const handleLogOut = () => {
        Cookies.remove('auth_token');  // Remove the token
        console.log("token removed!");
        console.log(Cookies.get('auth_token'));
        onLogOut();  // Call the function passed via props to trigger the state change
    };

    return (
        <>
            <div 
                className="login-box space-y-2 text-right text-4xl lg:text-3xl md:text-3xl font-bold mb-6"
                dir="rtl"
            >
                <p className="flex items-center pb-5 leading-relaxed">
                    می‌خواهید از حساب کاربری خود خارج شوید؟
                </p>
                <button
                    onClick={handleLogOut}
                    className="bg-teal-500 text-xl px-4 py-2 rounded-full text-white hover:bg-teal-600"
                    style={{ maxWidth: "150px" }}
                >
                    خروج
                </button>
            </div>
        </>
    );
};

export default LogOut;
