import React from "react";
import Navbar from "./Navbar";
import ProjectCart from "./ProjectCard";
import Dashborad from "./Dashboard";
import Footer from "./Footer";

function Projects() {
    return (
        <div>
            <ProjectCart />
            <div style={{marginTop:80}}/>
            <Footer />
        </div>
    )
}

export default Projects 