// src/components/UserForm.js
import React, { useState, useEffect } from 'react';
import Cookies from 'js-cookie';

const UserPanel= () => {
    const [name, setName] = useState('');
    const [storedName, setStoredName] = useState('');

    useEffect(() => {
        const savedName = localStorage.getItem('name');
        if (savedName) {
            setStoredName(savedName);
        }
        console.log(Cookies.get('auth_token'));
        
    }, []);

    const handleChange = (e) => {
        setName(e.target.value);
    };

    const handleSubmit = (e) => {
        e.preventDefault();
        localStorage.setItem('name', name);
        setStoredName(name);
    };

    const handleClear = () => {
        localStorage.removeItem('name');
        setStoredName('');
    };

    return (
        <div>
            <form onSubmit={handleSubmit}>
                <input
                    type="text"
                    value={name}
                    onChange={handleChange}
                    placeholder="Enter your name"
                />
                <button type="submit">Save Name</button>
            </form>
            {storedName && (
                <div>
                  
                    <h2>Stored Name: {storedName}</h2>
                    <button onClick={handleClear}>Clear Name</button>
                </div>
            )}
        </div>
    );
};

export default UserPanel;
