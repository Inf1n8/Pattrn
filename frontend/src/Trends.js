import axios from "axios";
import { useState, useEffect } from "react";
import Navbar from "./Navbar";
import { API_URL, GRAPH_URL } from "./Config";
// import ApexCharts from "apexcharts";
// import ReactApexChart from "react-apexcharts";
import ReactApexChart from "react-apexcharts";
import { ApexCharts } from "apexcharts";

export default function Trends() {
  const [win, setWindow] = useState("M");
  const [graphData, setGraphData] = useState({
    stepscount: [],
    heartrate: [],
    sleepDuration: [],
    spo2: [],
    steps: [],
    caloriesBurned: [],
    stress: [],
  });
  const graphProperties = {
    options: {
      chart: {
        id: "area-datetime",
        type: "area",
        height: 350,
        zoom: {
          autoScaleYaxis: true,
        },
      },
      annotations: {
        yaxis: [
          {
            y: 30,
            borderColor: "#999",
            label: {
              show: true,
              text: "Support",
              style: {
                color: "#fff",
                background: "#00E396",
              },
            },
          },
        ],
        xaxis: [
          {
            x: new Date("01 Sep 2022").getTime(),
            borderColor: "#999",
            yAxisIndex: 0,
            label: {
              show: true,
              text: "Rally",
              style: {
                color: "#fff",
                background: "#775DD0",
              },
            },
          },
        ],
      },
      dataLabels: {
        enabled: false,
      },
      markers: {
        size: 0,
        style: "hollow",
      },
      xaxis: {
        type: "datetime",
        min: new Date("15 Sep 2022").getTime(),
        tickAmount: 6,
      },
      tooltip: {
        x: {
          format: "dd MMM yyyy",
        },
      },
      fill: {
        type: "gradient",
        gradient: {
          shadeIntensity: 1,
          opacityFrom: 0.7,
          opacityTo: 0.9,
          stops: [0, 100],
        },
      },
    },
  };
  const updateData = (timeline) => {
    console.log(timeline);

    switch (timeline) {
      case "W":
        ApexCharts.exec(
          "area-datetime",
          "zoomX",
          new Date("09 Oct 2022").getTime(),
          new Date("16 Oct 2022").getTime()
        );
        break;
      case "M":
        ApexCharts.exec(
          "area-datetime",
          "zoomX",
          new Date("16 Sep 2022").getTime(),
          new Date("16 Oct 2022").getTime()
        );
        break;
      default:
    }
  };
  const userID = localStorage.getItem("userId");

  useEffect(() => {
    axios
      .get(`${API_URL}${GRAPH_URL}/${userID}?window=${win}`)
      .then((res) => {
        setGraphData({
          stepscount: [{ data: res.data["stepscount"] }],
          heartrate: [{ data: res.data["heartrate"] }],
          sleepDuration: [{ data: res.data["sleepDuration"] }],
          spo2: [{ data: res.data["spo2"] }],
          steps: [{ data: res.data["steps"] }],
          caloriesBurned: [{ data: res.data["caloriesBurned"] }],
          stress: [{ data: res.data["stress"] }],
        });
      })
      .catch((err) => {
        console.log(err.data);
      });
  }, [win]);

  return (
    <div>
      <Navbar />
      <h2 className="container">Heart Rate</h2>
      <div id="chart" className="container">
        <div className="toolbar">
          <button
            id="W"
            onClick={() => updateData("W")}
            className={win === "W" ? "active" : ""}
          >
            1 Week
          </button>
          &nbsp;
          <button
            id="M"
            onClick={() => updateData("M")}
            className={win === "M" ? "active" : ""}
          >
            1 Month
          </button>
          &nbsp;
        </div>
        <div id="chart-timeline">
          <ReactApexChart
            options={graphProperties.options}
            series={graphData["heartrate"]}
            type="area"
            height={350}
          />
        </div>
      </div>
    </div>
  );
}
