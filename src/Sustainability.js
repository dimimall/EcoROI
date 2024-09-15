import React from 'react';
import './Sustainability.css'; // Assuming you will use external CSS

const Sustainability = () => {
  return (
    <div className="sustainability-container">
      <div className="sustainability-content">
        <h1 className="sustainability-title">Measure for Sustainability</h1>
        <p className="sustainability-text">
          Sign up now to receive timely email alerts about
        </p>
        <div className="button-container">
          <button className="btn signup-btn">Sign Up</button>
          <button className="btn learnmore-btn">Learn More</button>
        </div>
      </div>
    </div>
  );
};

export default Sustainability;