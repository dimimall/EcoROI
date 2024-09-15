import React from 'react';
import './Navbar.css';
import logo from './fad_logo_juice.svg';
import MainBody from './MainBody.js';
import HomePage from './HomePage.js';
import Projects from './Projects.js';

function Navbar() {
    return (
        <nav className="navbar">
            <div className="navbar-left">
                <img src={logo} alt="logo" className="svg-inline"/>
                <a href="/" className="logo">
                    EcoROI
                </a>
            </div>
            <div className="navbar-center">
                <ul className="nav-links">
                     <li>
                        <a href="./HomePage">About Us</a>
                    </li>
                    <li>
                        <a href="./MainBody">How it Works</a>
                    </li>
                    <li>
                        <a href="./Projects">My Projects</a>
                    </li>
                    <li>
                        <a href="/contact">Contact</a>
                    </li>
                </ul>
            </div>
            <div className="navbar-right">
                <a href="/cart" className="cart-icon">
                    <i className="fas fa-shopping-cart"></i>
                    <span className="cart-count">Sign Out</span>
                </a>
                <a href="/account" className="user-icon">
                    <i className="fas fa-user"></i>
                </a>
            </div>
        </nav>
    );
};

export default Navbar