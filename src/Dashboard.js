import React from 'react';
import ProjectCard from './ProjectCard';
import './Dashboard.css'; // Assuming you want to add some CSS
import Rectangle1 from './Rectangle_19.png';
import Rectangle2 from './Rectangle19_1.png';
import Rectangle3 from './Rectangle_19_2.png'

const Dashboard = () => {
  const projects = [
    {
      title: 'Urban Heat Island Mitigation with Green Roofs',
      image: {Rectangle1},  // Replace with actual paths
      graphColor: 'green',
    },
    {
      title: 'Precision Farming for Sustainable Agriculture',
      image: {Rectangle2},  // Replace with actual paths
      graphColor: 'red',
    },
    {
      title: 'Development of Data Center',
      image: {Rectangle3},  // Replace with actual paths
      graphColor: 'orange',
    },
  ];

  return (
    <div className="dashboard">
      <h2>Dashboard</h2>
      <button className="create-project-btn">Create a new Project</button>
      <div className="project-grid">
        {projects.map((project, index) => (
          <ProjectCard
            key={index}
            title={project.title}
            image={project.image}
            graphColor={project.graphColor}
          />
        ))}
      </div>
    </div>
  );
};

export default Dashboard;