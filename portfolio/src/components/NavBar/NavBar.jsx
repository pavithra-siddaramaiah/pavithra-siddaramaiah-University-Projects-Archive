import React, { useState } from 'react';
import { slide as Menu } from 'react-burger-menu';
import { Link, useLocation } from 'react-router-dom';
import './NavBar.css';

const NavBar = () => {
    const [menuOpen, setMenuOpen] = useState(false);
    const location = useLocation();
    const path = location.pathname;

    const handleStateChange = (state) => {
        setMenuOpen(state.isOpen);
    };

    const closeMenu = () => {
        setMenuOpen(false);
    };

    return (
        <Menu 
            isOpen={menuOpen}
            onStateChange={(state) => handleStateChange(state)} >
        
            <Link to='/' onClick={closeMenu}
                className={`menu-item ${path === '/' ? 'active-item' : ''}`}>
                Home
            </Link>
            <Link to='/about' onClick={closeMenu}
                className={`menu-item ${path === '/about' ? 'active-item' : ''}`}>
                About
            </Link>
            <Link to='/projects' onClick={closeMenu}
                className={`menu-item ${path === '/projects' ? 'active-item' : ''}`}>
                Projects
            </Link>
            <Link to='/skills' onClick={closeMenu}
                className={`menu-item ${path === '/skills' ? 'active-item' : ''}`}>
                Skills
            </Link>
            <Link to='/contact' onClick={closeMenu}
                className={`menu-item ${path === '/contact' ? 'active-item' : ''}`}>
                Contact
            </Link>
        </Menu>
    );
};

export default NavBar;
