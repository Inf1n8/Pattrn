import axios from "axios";
import { useState, useEffect } from "react";
import ButtonGroup from "react-bootstrap/ButtonGroup";
import ToggleButton from "react-bootstrap/ToggleButton";
import Navbar from "./Navbar";
import Spinner from "react-bootstrap/Spinner";
import { API_URL, STATS_URL, GOALS_URL } from "./Config";

export default function Progress() {
  const [loading, setLoading] = useState(false);
  const [stats, setStats] = useState({
    stress: 0,
    sleep: 0,
    steps: 0,
    heartRate: 0,
    bloodOxygen: 0,
  });
  const [goalState, setGoalState] = useState({
    stress: "",
    sleep: "",
    steps: "",
    heartRate: "",
    bloodOxygen: "",
  });
  const userID = localStorage.getItem("userId");

  const [radioValue, setRadioValue] = useState("day");
  const radios = [
    { name: "Day", value: "day" },
    { name: "Week", value: "week" },
    { name: "Month", value: "month" },
  ];

  const status = [
    {
      fieldName: "Stress",
      name: "stress",
      text: "You are more stressed than usual. Remember to take breaks after a long working session.",
    },
    {
      fieldName: "Sleep",
      name: "sleep",
      text: "You are more stressed than usual. Remember to take breaks after a long working session.",
    },
    {
      fieldName: "Steps",
      name: "steps",
      text: "You are more stressed than usual. Remember to take breaks after a long working session.",
    },
    {
      fieldName: "Heart Rate",
      name: "heartRate",
      text: "You are more stressed than usual. Remember to take breaks after a long working session.",
    },
    {
      fieldName: "Blood Oxygen",
      name: "bloodOxygen",
      text: "You are more stressed than usual. Remember to take breaks after a long working session.",
    },
  ];

  useEffect(() => {
    let window = null;
    if (radioValue === "day") {
      window = "D";
    } else if (radioValue === "week") {
      window = "W";
    } else {
      window = "M";
    }
    setLoading(true);
    axios
      .get(`${API_URL}${STATS_URL}/${userID}?window=${window}`)
      .then((res) => {
        console.log(res.data);
        let data = res.data;
        setStats({
          steps: data["steps"]["average"],
          sleep: data["sleep"]["average"],
          stress: data["stress"]["average"],
          bloodOxygen: data["bloodOxygen"]["average"],
          heartRate: data["heartRate"]["average"],
        });
        setLoading(false);
      })
      .catch((err) => {
        console.log(err);
        setLoading(false);
      });

    axios
      .get(`${API_URL}${GOALS_URL}/${userID}`, {
        headers: {
          "Content-Type": "application/json",
        },
      })
      .then(function (response) {
        let res = JSON.parse(response.data);
        setGoalState(res);
      })
      .catch((err) => {
        console.log(err.response.data);
      });
  }, [radioValue]);

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
                  variant="outline-danger"
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
          <div
            style={{
              display: loading ? "block" : "none",
              position: "relative",
              left: "50%",
            }}
          >
            <Spinner animation="border" variant="dark" />
          </div>
          <div style={{ display: loading ? "none" : "block" }}>
            {status.map((ele, ind) => {
              return (
                <div
                  key={ind}
                  style={{
                    height: "100px",
                    boxShadow: "0 4px 8px 0 rgba(0,0,0,0.2)",
                    borderRadius: "5px",
                  }}
                  className="d-flex flex-row align-items-center mt-3 px-1"
                >
                  <h5
                    style={{ width: "150px", flexGrow: 3, textAlign: "center" }}
                  >
                    {ele["fieldName"]}
                  </h5>
                  <div
                    className="px-2"
                    style={{ width: "150px", flexGrow: 2, textAlign: "center" }}
                  >
                    Average:{" "}
                    <span className="circle">{stats[ele["name"]]}</span>
                  </div>
                  <div
                    className="flex-end"
                    style={{ width: "150px", flexGrow: 3, textAlign: "center" }}
                  >
                    Target: {goalState[ele["name"]]}
                  </div>
                  {/* <div className="d-flex align-items-center"></div> */}
                </div>
              );
            })}
          </div>
        </div>
      </div>
    </div>
  );
}
