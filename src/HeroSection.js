import React from 'react';
import './HeroSection.css';
import { randomBinomial } from 'd3';
import IconMap from './map_image.png'

function HeroSection() {

    return (
        <div className="hero-container">
          <div className="hero-content">
            <h1>Sustainability Project Management For Maximizing S - ROI</h1>
            <p>
              Welcome to our platform, where we provide a cutting-edge, data-driven project management platform that integrates Copernicus satellite data with advanced Sustainability Return on Investment (S-ROI) calculations. This approach enables organizations, governments, and stakeholders to not only track their sustainability efforts in real-time but also prioritize the highest-impact actions, ensuring that taxpayers' money invested leads to measurable progress toward global goals.
            </p>
            <button>Learn More</button>
          </div>
          <div className='hero-content2'>
            <img src={IconMap} alt="iconmap"/>
            <button>Start Measuring</button>
          </div>
        </div>
      );
};

export default HeroSection