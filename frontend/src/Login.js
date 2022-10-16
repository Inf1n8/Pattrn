import React, { useState } from "react";
import Button from "react-bootstrap/Button";
import axios from "axios";
import Form from "react-bootstrap/Form";
import { API_URL, LOGIN_URL } from "./Config";

export default function Login() {
  const isAuthenticated = localStorage.getItem("isAuthenticated");
  if (isAuthenticated) {
    window.location.pathname = "/";
  }

  const [userData, setUserData] = useState({ email: "", password: "" });

  const handleInputChange = (e) => {
    setUserData((prevState) => {
      return {
        ...prevState,
        [e.target.name]: e.target.value,
      };
    });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    console.log(userData);
    let jsonData = JSON.stringify(userData);
    axios
      .post(`${API_URL}/${LOGIN_URL}`, jsonData, {
        headers: {
          "Content-Type": "application/json",
        },
      })
      .then(function (response) {
        console.log(response.data);
        localStorage.setItem("isAuthenticated", "true");
        localStorage.setItem("userId", response.data["id"]);
        window.location.pathname = "/";
      })
      .catch((err) => {
        console.log(err.response.data);
        alert(err.response.data["message"]);
      });
  };

  return (
    <div className="loginPage">
      <div className="loginContainer">
        <Form>
          <div className="loginLogo"></div>
          <h1 className="mb-5 text-center">Medical Report Card</h1>
          <Form.Group className="mb-3" controlId="formBasicEmail">
            <Form.Control
              type="email"
              placeholder="Email ID"
              name="email"
              onChange={(e) => handleInputChange(e)}
            />
          </Form.Group>

          <Form.Group className="mb-3" controlId="formBasicPassword">
            <Form.Control
              type="password"
              placeholder="Password"
              name="password"
              onChange={(e) => handleInputChange(e)}
            />
          </Form.Group>
          <div className="d-flex flex-row justify-content-center align-items-center mt-4">
            <Button
              className={"submitBtn"}
              variant="primary"
              type="submit"
              onClick={handleSubmit}
            >
              Log In
            </Button>
          </div>
          <div className="mt-3 text-center">Forgot password?</div>
        </Form>
      </div>
    </div>
  );
}
