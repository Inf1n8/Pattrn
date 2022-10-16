import React, { useState } from "react";
import Button from "react-bootstrap/Button";

const CardGoal = ({
  fieldName,
  name,
  values,
  unit,
  selectedVal,
  setUpdatedGoal,
}) => {
  return (
    <div className="goalCard d-flex flex-row align-items-center mt-3 justify-content-between">
      <div className="d-flex flex-row align-items-center">
        <div className={name} />
        <h6 className="mx-3">{fieldName}</h6>
      </div>
      <select
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
      </select>
    </div>
  );
};

export default function Goals() {
  const [goalState, setGoalState] = useState({
    stress: "",
    sleep: "",
    steps: "",
    heartRate: "",
    bloodOxygen: "",
  });

  const goalTypes = [
    {
      fieldName: "Stress",
      name: "stress",
      values: [
        "",
        "0-9",
        "10-19",
        "20-29",
        "30-39",
        "40-49",
        "50-59",
        "60-69",
        "70-79",
      ],
      unit: "val",
    },
    {
      fieldName: "Sleep",
      name: "sleep",
      values: ["", "6-7", "7-8", "8-9", "9-10"],
      unit: "hours",
    },
    {
      fieldName: "Steps",
      name: "steps",
      values: [
        "",
        "2000-2999",
        "3000-3999",
        "4000-4999",
        "5000-5999",
        "6000-6999",
        "7000-7999",
        "8000-8999",
        "9000+",
      ],
      unit: "steps",
    },
    {
      fieldName: "Heart Rate",
      name: "heartRate",
      values: ["", "65-74", "75-84", "85-95"],
      unit: "bpm",
    },
    {
      fieldName: "Blood Oxygen",
      name: "bloodOxygen",
      values: ["", "96-97.99", "98-100"],
      unit: "%",
    },
  ];

  const setUpdatedGoal = (name, value) => {
    setGoalState((prevState) => {
      return {
        ...prevState,
        [name]: value,
      };
    });
  };

  return (
    <div>
      <div className="container">
        <div className="goalsHeaderContainer d-flex justify-content-center align-items-center mt-3">
          <div className="goalsLogo"></div>
          <h3>Health Goals</h3>
        </div>
        <div className="d-flex flex-column justify-content-center align-items-center">
          {goalTypes.map((ele, ind) => {
            return (
              <CardGoal
                key={ind}
                fieldName={ele["fieldName"]}
                name={ele["name"]}
                values={ele["values"]}
                unit={ele["unit"]}
                selectedVal={goalState[ele["name"]]}
                setUpdatedGoal={setUpdatedGoal}
              />
            );
          })}
        </div>
        <div className="mt-5 d-flex justify-content-center">
          <Button variant="success">Save</Button>
        </div>
      </div>
    </div>
  );
}
