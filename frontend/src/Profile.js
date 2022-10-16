import React, { useState } from "react";
import Card from 'react-bootstrap/Card';
import Navbar from "./Navbar";

export default function Profile() {

  const handleHealthGoals = (e) => {
    window.location.pathname = "/";
  };

  const handleHealthInfo = (e) => {
    window.location.pathname = "/";
  };

  return (
    <div>
    
      <Navbar />
      <div className="ProfilePage">
      <div className="ProfileCard">
      <h3 className="mb-5 text-center">Edit Your Profile</h3>
      <Card onClick={handleHealthGoals} style={{ cursor: "pointer" }}>
    <Card.Body>Health Goals</Card.Body>
    </Card>
    <br />
    <Card onClick={handleHealthInfo} style={{ cursor: "pointer" }}>
    <Card.Body>Health Info</Card.Body>
    </Card>
    </div>
    </div>
    </div>
    
  );
}
