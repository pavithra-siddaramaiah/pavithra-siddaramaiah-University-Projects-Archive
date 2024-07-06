import React from 'react'
import "./About.css"
import Header from '../Header/Header'

const About = () => {
  return (
    <div>
        <div className='section-container'>
        <Header
        heading="About Me"
        subHeading="Full Stack Engineer | Blogger" />
       
        </div>
      
      <div className='about-main'>
        <div className='about-main-left'>
            <h3 className='about-sub-heading'>Developer</h3>
            <p className='about-sub-heading-details'>
              I’m a software engineer. building software for people and businesses. I love building software that solves real-world problems, add value to society through technology.
            </p>
            <h3 className='about-sub-heading'>Blogger</h3>
            <p className='about-sub-heading-details'>
              I've been writing blogs from around 3 years now, i used to write on Quora then i moved to hashnode now. you can read my articles here!
            </p>
        </div>
       </div>
       
    </div>
  )
}

export default About