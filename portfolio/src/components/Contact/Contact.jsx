import React from 'react'
import { useForm, ValidationError } from '@formspree/react';
import Header from '../Header/Header'
import github from "./../../assets/github.png"
import linkedin from "./../../assets/linkedin.png"
import "./Contact.css"

const Contact = () => {
    const [state, handleSubmit] = useForm("mdobenlw");
  if (state.succeeded){
      setTimeout(() => {
        document.getElementById("contact-form").reset();
      }, 2500)
  }
  return (
    <div className='section-container'>
      <Header
        heading="Get in touch."
        subHeading="Interested to collaborate? Feel free to drop me an email.">
      </Header>
      <div className='contact-form-container'>
        {
            state.succeeded &&
            <div className='alert'>
                Thanks for the submission!
            </div>
        }
        <form className='contact-form' onSubmit={handleSubmit}
        id='contact-form'>
          <input type="email" className='input-box email-input'
            placeholder='Your Email Id' name='email' required/>
            <ValidationError
              prefix="Email"
              field="email"
              errors={state.errors}
            />
          <textarea type="text" placeholder='Your Message' name='message'
            className='input-box body-input' required></textarea>
          <ValidationError
          prefix="Message"
          field="message"
          errors={state.errors}
        />
          <button type="submit" className="contact-btn"
          disabled={state.submitting}>
            Send Email
          </button>
        </form>
      </div>
      <div className='social-icons-container'>
        <a href="https://github.com/pavithra-siddaramaiah"
          className='social-icon'
          target="_blank" rel="noreferrer">
          <img src={github} alt='github' loading="lazy"/>
        </a>
        <a href="https://www.linkedin.com/in/pavithra-siddaramaiah-921078172/"
          className='social-icon'
          target="_blank" rel="noreferrer">
          <img src={linkedin} alt='linkedin' loading="lazy"/>
        </a>
        
        
      </div>
      
      
    </div>
  )
}

export default Contact