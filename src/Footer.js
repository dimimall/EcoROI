import React from 'react';
import './Footer.css'; // Make sure to create a CSS file for styling

const Footer = () => {
  return (
    <footer className="footer">
      <div className="footer-container">
        <div className="subscribe-section">
          <h2 className="footer-title">ECOROI</h2>
          <p>Subscribe to keep up with the latest news</p>
          <form className="subscribe-form">
            <input type="email" placeholder="enter your email..." required />
            <button type="submit">→</button>
          </form>
          <p className="privacy-text">
            By submitting this form, you acknowledge that you have read the terms of our Privacy Statement
          </p>
        </div>

        <div className="links-section">
          <div className="column">
            <ul>
              <li><strong>Solutions</strong></li>
              <li>Open EO</li>
              <li>SGS</li>
              <li>Moncler</li>
              <li>Copernicus</li>
              <li>Siemens</li>
            </ul>
          </div>
          <div className="column">
            <ul>
              <li><strong>Pages</strong></li>
              <li>Home</li>
              <li>About</li>
              <li>Services</li>
              <li>Contact</li>
              <li>Terms and Conditions</li>
            </ul>
          </div>
        </div>

        <div className="social-media-section">
          <p>Copyright © EcoROI 2024</p>
          <div className="social-icons">
            <a href="#"><i className="fab fa-facebook"></i></a>
            <a href="#"><i className="fab fa-linkedin"></i></a>
            <a href="#"><i className="fab fa-twitter"></i></a>
          </div>
        </div>
      </div>
    </footer>
  );
};

export default Footer;