import React from 'react'
import "./Header.css"

const Header = ({heading, subheading}) => {
  return (
    <div className="header-container">
        <h1> { heading }</h1>
        <p>{ subheading }</p>
    </div>
  )
}

export default Header