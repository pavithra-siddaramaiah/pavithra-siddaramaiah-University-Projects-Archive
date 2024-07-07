import React from 'react'
import {useState, useEffect} from 'react'
import {Link} from 'react-router-dom'
import "./Home.css"

const Home = () => {
    const [showModal, setShowModal] = useState(false);

    useEffect(() => {
        const timer = setTimeout(() => {
            setShowModal(true);
        }, 2400);
        return () => clearTimeout(timer); // Clean up the timer
    }, []);

    const closeModal = () => {
        setShowModal(false);
    };

    return (
        <div className="home-container">
            
            <div className="header-text">
                <h1>Welcome to my portfolio!</h1>
                <h2>This is Pavithra Siddaramaiah, a <u>Job Seeker</u>.</h2>
            </div>
            <div className="header-btns">
                <Link className="btn btn-white" to="/about">
                    <p className="btn-text">Know more about me</p>
                </Link>
                <Link className="btn btn-transparent" to="/contact">
                    <p className="btn-text">Contact with me</p>
                </Link>
            </div>
            <div className="splash-image">
                
            </div>
        </div>
    );
};

export default Home