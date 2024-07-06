import React from 'react'
import Header from '../Header/Header'
import github from "./../../assets/github.png"
import linkedin from "./../../assets/linkedin.png"
import "./Contact.css"

const Contact = () => {
  return (
    <div className="section-container">
        <Header heading = "Get in touch" subheading= "Interested to collaborate? Feel free to drop me an email." />

    <div className = "social-icons-container">
    <a href = "https://github.com/pavithra-siddaramaiah" className= "social-icon" target="_blank" >
        <img src = {github} alt = "github logo" />
    </a>
    <a href = "https://www.linkedin.com/in/pavithra-siddaramaiah-921078172/" className= "social-icon" target="_blank" >
        <img src = {linkedin} alt = "linkedin logo" />
    </a>
    </div>
    </div>
    

  )
}

export default Contact