import React from 'react';
import './ProjectCard.css'; // Assuming you want to add some CSS
import Rectangle1 from './Rectangle_19.png';
import Rectangle2 from './Rectangle19_1.png';
import Rectangle3 from './Rectangle_19_2.png'
import Combo1 from './ComboChart.png';
import Combo2 from './ComboChart1.png';
import Combo3 from './ComboChart2.png';


function ProjectCard() {
  return (
    <div className='container'>
      <div className="project-card">
        <img src={Rectangle1} className="project-image" />
        <div className="project-info">
          <h3>Urban Heat Island Mitigation with Green Roofs</h3>
         <div className={`graph-icon ${Combo1}`}></div> {/* Example: graphColor could be 'green', 'orange', etc. */}
        </div>
      </div>
      <div className="project-card">
        <img src={Rectangle2} className="project-image" />
        <div className="project-info">
          <h3>Urban Heat Island Mitigation with Green Roofs</h3>
         <div className={`graph-icon ${Combo2}`}></div> {/* Example: graphColor could be 'green', 'orange', etc. */}
        </div>
      </div>
      <div className="project-card">
        <img src={Rectangle3} className="project-image" />
        <div className="project-info">
          <h3>Urban Heat Island Mitigation with Green Roofs</h3>
         <div className={`graph-icon ${Combo3}`}></div> {/* Example: graphColor could be 'green', 'orange', etc. */}
        </div>
      </div>
    </div>
    
  );
};

export default ProjectCard;