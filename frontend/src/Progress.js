import { useState, useEffect } from "react";
import ButtonGroup from "react-bootstrap/ButtonGroup";
import ToggleButton from "react-bootstrap/ToggleButton";
import Navbar from "./Navbar";

export default function Progress() {
  const [stats, setStats] = useState({
    stress: 45,
    sleep: 7.5,
    steps: 8324,
    heartRate: 85,
    bloodOxygen: 98,
  });

  const [checked, setChecked] = useState(false);
  const [radioValue, setRadioValue] = useState("day");
  const radios = [
    { name: "Day", value: "day" },
    { name: "Weekly", value: "weekly" },
    { name: "Month", value: "month" },
  ];

  const status = [
    {
      fieldName: "Stress",
      name: "stress",
      marks: [
        { value: 0, label: "0" },
        { value: 20, label: "20" },
        { value: 40, label: "40" },
        { value: 60, label: "60" },
        { value: 80, label: "80" },
        { value: 100, label: "100" },
      ],
      //   values: [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100],
      min: 0,
      max: 100,
      text: "You are more stressed than usual. Remember to take breaks after a long working session.",
    },
    {
      fieldName: "Sleep",
      name: "sleep",
      marks: [
        { value: 0, label: "0" },
        { value: 4, label: "4" },
        { value: 8, label: "8" },
        { value: 12, label: "12" },
        { value: 16, label: "16" },
      ],
      //   values: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14],
      min: 0,
      max: 15,
      text: "You are more stressed than usual. Remember to take breaks after a long working session.",
    },
    {
      fieldName: "Steps",
      name: "steps",
      marks: [
        { value: 0, label: "0" },
        { value: 2000, label: "2000" },
        { value: 4000, label: "4000" },
        { value: 6000, label: "6000" },
        { value: 8000, label: "8000" },
        { value: 10000, label: "10000" },
      ],
      //   values: [0, 2000, 4000, 6000, 8000, 10000],
      min: 0,
      max: 10000,
      text: "You are more stressed than usual. Remember to take breaks after a long working session.",
    },
    {
      fieldName: "Heart Rate",
      name: "heartRate",
      marks: [
        { value: 0, label: "0" },
        { value: 25, label: "25" },
        { value: 50, label: "50" },
        { value: 75, label: "75" },
        { value: 100, label: "100" },
        { value: 125, label: "125" },
        { value: 150, label: "150" },
        { value: 175, label: "175" },
      ],
      //   values: [0, 25, 50, 75, 100, 125, 150, 175],
      min: 0,
      max: 190,
      text: "You are more stressed than usual. Remember to take breaks after a long working session.",
    },
    {
      fieldName: "Blood Oxygen",
      name: "bloodOxygen",
      marks: [
        { value: 0, label: "0" },
        { value: 25, label: "25" },
        { value: 50, label: "50" },
        { value: 75, label: "75" },
        { value: 100, label: "100" },
      ],
      //   values: [0, 25, 50, 75, 100],
      min: 0,
      max: 100,
      text: "You are more stressed than usual. Remember to take breaks after a long working session.",
    },
  ];

  //   useEffect(() => {}, []);
  return (
    <div>
      <Navbar />
    
    <div className="d-flex justify-content-center mt-3 mb-5">
      <div className="d-flex flex-column progressCard mx-2">
        <h2 style={{ textAlign: "center" }}>Deep Dive</h2>
        <div className="d-flex justify-content-center mt-2 mb-4">
          <ButtonGroup>
            {radios.map((radio, idx) => (
              <ToggleButton
                key={idx}
                id={`radio-${idx}`}
                type="radio"
                variant={idx % 2 ? "outline-success" : "outline-danger"}
                name="radio"
                value={radio.value}
                checked={radioValue === radio.value}
                onChange={(e) => setRadioValue(e.currentTarget.value)}
              >
                {radio.name}
              </ToggleButton>
            ))}
          </ButtonGroup>
        </div>
        {status.map((ele, ind) => {
          return (
            <div
              key={ind}
              style={{
                height: "100px",
                boxShadow: "0 4px 8px 0 rgba(0,0,0,0.2)",
                borderRadius: "5px",
              }}
              className="d-flex flex-row justify-content-around align-items-center mt-3 px-1"
            >
              <h5 style={{ width: "150px" }}>{ele["fieldName"]}</h5>
              <div className="d-flex align-items-center">
                <div className="px-2">
                  Average: <span className="circle">{stats[ele["name"]]}</span>
                </div>
                <div>Target: 7000-8000</div>
              </div>
            </div>
          );
        })}
      </div>
    </div>
    </div>
  );
}
