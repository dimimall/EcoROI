import React, { useState } from 'react';
import './CreateProject.css'; 
import {
    MapContainer,
    TileLayer,
  } from "react-leaflet";
import "leaflet/dist/leaflet.css";


const CreateProject = () => {
  const [projectName, setProjectName] = useState('');
  const [location, setLocation] = useState('');
  const [startDate, setStartDate] = useState('');
  const [returnDate, setReturnDate] = useState('');
  const [selectedSDG, setSelectedSDG] = useState('');
  const [selectedIndicators, setSelectedIndicators] = useState('');

  const handleStartDateChange = (e) => setStartDate(e.target.value);
  const handleReturnDateChange = (e) => setReturnDate(e.target.value);
  const handleSDGChange = (e) => setSelectedSDG(e.target.value);
  const handleIndicatorsChange = (e) => setSelectedIndicators(e.target.value);

  const handleProjectNameChange = (e) => {
    setProjectName(e.target.value);
  };

  const handleLocationChange = (e) => {
    setLocation(e.target.value);
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    // Submit the form (you can add your logic here)
    console.log("Project Name:", projectName);
    console.log("Location:", location);
    console.log("Start Date:", startDate);
    console.log("Return Date:", returnDate);
    console.log("Selected SDG:", selectedSDG);
    console.log("Selected Indicators:", selectedIndicators);
  };

  return (
    <div className="create-project-container">
      <h1 className="title">Create a New Project</h1>
      <hr />
      <form onSubmit={handleSubmit}>
        <div className="form-group">
            <div className="section-title">
                <span className="section-number">1</span>
                <span>Project Name</span>
            </div>
          <input
            type="text"
            placeholder="Enter your project’s name"
            value={projectName}
            onChange={handleProjectNameChange}
            className="input-field"
          />
        </div>
        <div className="form-group">
            <div className="section-title">
                <span className="section-number">2</span>
                <span>Location</span>
            </div>
          <input
            type="text"
            placeholder="Enter your location"
            value={location}
            onChange={handleLocationChange}
            className="input-field"
          />
        </div>
        <div className="row" style={{ gap: "10px" }}></div>
        <MapContainer
            style={{
            height: "300px",
            width: "600px",
            }}
            center={[31.432026740690574, 120.8439179532812]}
            zoom={8}
        >
            {/* add google map tile url  */}
            <TileLayer
                attribution="Google Maps"
                url="https://www.google.cn/maps/vt?lyrs=m@189&gl=cn&x={x}&y={y}&z={z}"
            />
        </MapContainer>

        <div className="form-section">
          <div className="section-title">
            <span className="section-number">3</span>
            <span>Duration</span>
          </div>
          <div className="form-group">
            <input 
              type="date" 
              placeholder="Start Date" 
              value={startDate} 
              onChange={handleStartDateChange} 
              className="input-field2" 
            />
            <input 
              type="date" 
              placeholder="Return Date" 
              value={returnDate} 
              onChange={handleReturnDateChange} 
              className="input-field2" 
            />
          </div>
        </div>

        {/* Select SDG Section */}
        <div className="form-section">
          <div className="section-title">
            <span className="section-number">4</span>
            <span>Select SDG</span>
          </div>
          <div className="form-group">
            <select 
              value={selectedSDG} 
              onChange={handleSDGChange} 
              className="input-field2">
              <option value="">Select SDG</option>
              <option value="SDG 1">SDG 1</option>
              <option value="SDG 2">SDG 2</option>
              {/* Add more SDG options as needed */}
            </select>
          </div>
        </div>

        {/* Select Sustainability Indicators Section */}
        <div className="form-section">
          <div className="section-title">
            <span className="section-number">5</span>
            <span>Select Sustainability Indicators</span>
          </div>
          <div className="form-group">
            <select 
              value={selectedIndicators} 
              onChange={handleIndicatorsChange} 
              className="input-field2">
              <option value="">Select Sustainability Indicators</option>
              <option value="Indicator 1">Indicator 1</option>
              <option value="Indicator 2">Indicator 2</option>
              {/* Add more indicator options as needed */}
            </select>
          </div>
        </div>
        <button type="submit" className="submit-btn">Create Project</button>
      </form>
    </div>
  );
};

export default CreateProject;