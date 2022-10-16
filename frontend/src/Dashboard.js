import React, { useState } from "react";
import Button from "react-bootstrap/Button";
import Form from 'react-bootstrap/Form';
import Modal from 'react-bootstrap/Modal';
import Navbar from "./Navbar";
import RatingPage from "./Rating";




const CardGoal = ({
  fieldName,
  name,
//   values,
//   unit,
//   selectedVal,
//   setUpdatedGoal,
}) => {
  return (
    <div className="goalCard d-flex flex-row align-items-center mt-3 justify-content-between">
      <div className="d-flex flex-row align-items-center">
        <div className={name} />
        <h6 className="mx-3">{fieldName}</h6>
      </div>
      {/* <select
        name={name}
        value={selectedVal}
        onChange={(e) => {
          setUpdatedGoal(name, e.target.value);
        }}
      >
        {values.map((e, key) => {
          return (
            <option key={key} value={e}>
              {`${e} ${unit}`}
            </option>
          );
        })}
      </select> */}
    </div>
  );
};



export default function Goals() {
    const [show, setShow] = useState(false);

  const handleClose = () => setShow(false);
  const handleShow = () => setShow(true);
//   const [goalState, setGoalState] = useState({
//     stress: "",
//     sleep: "",
//     steps: "",
//     heartRate: "",
//     bloodOxygen: "",
//   });


  const goalTypes = [
    {
      fieldName: "Stress levels are 2% higher than usual. Remember to take breaks!",
      name: "stress",
    },
    {
      fieldName: "You slept 1.5 hour more than your goal. Good job!",
      name: "sleep",
    },
    {
      fieldName: "Yesterday’s steps were only 100 away from goal. Let’s try again to get to 10K today!",
      name: "steps",
    },
    {
      fieldName: "Heart rate and Blood Oxygen are at normal levels.",
      name: "heartRate",
    },
    // {
    //   fieldName: "Blood Oxygen is at normal levels",
    //   name: "bloodOxygen",
    // },
  ];

//   const setUpdatedGoal = (name, value) => {
//     setGoalState((prevState) => {
//       return {
//         ...prevState,
//         [name]: value,
//       };
//     });
//   };

const ratingChanged = (newRating) => {
    console.log(newRating);
  };

  return (
    <div>
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
                // values={ele["values"]}
                // unit={ele["unit"]}
                // selectedVal={goalState[ele["name"]]}
                // setUpdatedGoal={setUpdatedGoal}
              />
            );
          })}
        </div>

        
        {/* <RatingPage /> */}
        
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
          
            <Form.Group className="mb-3" controlId="exampleForm.ControlInput1">
            
              {/* <Form.Label>Email address</Form.Label>
              <Form.Control
                type="email"
                placeholder="name@example.com"
                autoFocus
              />
            </Form.Group>
            <Form.Group
              className="mb-3"
              controlId="exampleForm.ControlTextarea1"
            >
              <Form.Label>Example textarea</Form.Label> */}
              <Form.Control as="textarea" rows={3} />
            </Form.Group>
          </Form>
        </Modal.Body>
        <Modal.Footer>
          {/* <Button variant="secondary" onClick={handleClose}>
            Close
          </Button> */}
          <Button variant="primary" onClick={handleClose}>
            Submit
          </Button>
        </Modal.Footer>
      </Modal>
      </div>
    </div>
  );
}