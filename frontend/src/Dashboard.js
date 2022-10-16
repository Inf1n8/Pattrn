import React, { useState } from "react";
import Button from "react-bootstrap/Button";
import axios from "axios";
import { API_URL, LOGIN_URL } from "./Config";
import Container from 'react-bootstrap/Container';
import Card from 'react-bootstrap/Card';
import Navbar from "./Navbar";

export default function Dashboard() {

  const handleViewMore = (e) => {
    window.location.pathname = "/";
  };

  return (
    <div>
      <Navbar />
      <div className="DashboardPage">
      <div className="DashboardCard">
    <Card style={{ width: '18rem' }}>
      {/* <Card.Img variant="top" src="./assets/dashboard_picture.png" /> */}
      <div className="randomImg"></div>
      <Card.Body>
        <Card.Title>Hello Jane!</Card.Title>
        <Card.Text>
        Your vitals are looking healthy. Stress levels are a little higher than average. You are on track to achieve your week health goals!
        </Card.Text>
        <Button variant="primary"
        onClick={handleViewMore}>View More</Button>
      </Card.Body>
    </Card>
    </div>
    </div>

    </div>
    
  );
}
