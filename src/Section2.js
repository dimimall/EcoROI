import React from "react";
import './Section2.css';
import Iconframe1 from './Frame.png'
import Iconframe2 from './Frame2.png';
import Iconcontent from './Content.png';


function Section2() {
    return (
        <div className="section2-container">
            <h1>Explore some of the Sustainability Metrics</h1>
            <div className="section2-content">
                <img src={Iconframe1} alt="frame1" style={{height:50,marginTop:70}}/>
                <img src={Iconcontent} alt="content"/>
                <img src={Iconframe2} alt="frame2" style={{height:50,marginTop:70}}/>
            </div>
        </div>
    )
}

export default Section2