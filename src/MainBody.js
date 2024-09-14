import React from 'react';
import CreateProject from './CreateProject';

function MainBody() {
    return(
        <div className="MainBody">
            <div className="row" style={{ gap: "10px" }}></div>
            <CreateProject />
        </div>
    );
};

export default MainBody