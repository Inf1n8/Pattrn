import React, { useState } from "react";
import Button from "react-bootstrap/Button";
import Form from "react-bootstrap/Form";
import Modal from "react-bootstrap/Modal";
import Navbar from "./Navbar";

const CardGoal = ({ fieldName, name }) => {
  return (
    <div className="goalCard d-flex flex-row align-items-center mt-3 justify-content-between">
      <div className="d-flex flex-row align-items-center">
        <div className={name} />
        <h6 className="mx-3">{fieldName}</h6>
      </div>
    </div>
  );
};

export default function Goals() {
  const [show, setShow] = useState(false);

  const handleClose = () => setShow(false);
  const handleShow = () => setShow(true);

  const goalTypes = [
    {
      fieldName:
        "Stress levels are 2% higher than usual. Remember to take breaks!",
      name: "stress",
    },
    {
      fieldName: "You slept 1.5 hour more than your goal. Good job!",
      name: "sleep",
    },
    {
      fieldName:
        "Yesterday’s steps were only 100 away from goal. Let’s try again to get to 10K today!",
      name: "steps",
    },
    {
      fieldName: "Heart rate and Blood Oxygen are at normal levels.",
      name: "heartRate",
    },
  ];

  const ratingChanged = (newRating) => {
    console.log(newRating);
  };

  return (
    <div>
      <div className="bgImg"></div>
      <div style={{ position: "relative" }}>
        <Navbar />
        <div className="container">
          <div className="goalsHeaderContainer d-flex justify-content-center align-items-center mt-3">
            <div className="dashboardLogo"></div>
            <h3>Hello Jane!</h3>
          </div>
          <div className="d-flex flex-column justify-content-center align-items-center">
            {goalTypes.map((ele, ind) => {
              return (
                <CardGoal
                  key={ind}
                  fieldName={ele["fieldName"]}
                  name={ele["name"]}
                />
              );
            })}
          </div>
          <div className="mt-5 d-flex justify-content-center">
            <Button variant="primary" onClick={handleShow}>
              Add Note
            </Button>
          </div>

          <Modal show={show} onHide={handleClose}>
            <Modal.Header closeButton>
              <Modal.Title>Notes</Modal.Title>
            </Modal.Header>
            <Modal.Body>
              <Form>
                <Form.Group
                  className="mb-3"
                  controlId="exampleForm.ControlInput1"
                >
                  <Form.Control as="textarea" rows={3} />
                </Form.Group>
              </Form>
            </Modal.Body>
            <Modal.Footer>
              <Button variant="primary" onClick={handleClose}>
                Submit
              </Button>
            </Modal.Footer>
          </Modal>
        </div>
      </div>
    </div>
  );
}
