import React from "react";
import ReactDOM from "react-dom/client";
import "bootstrap/dist/css/bootstrap.min.css";
import "./index.css";
import { BrowserRouter, Route, Routes } from "react-router-dom";
import PageNotFound from "./PageNotFound";
import ProtectedRoute from "./ProtectedRoute";
import Login from "./Login";
import Goals from "./Goals";
import Progress from "./Progress";
import Dashboard from "./Dashboard";

const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(
  <BrowserRouter>
    <Routes>
      <Route exact path="/" element={<ProtectedRoute />}>
        <Route exact path="/" element={<Dashboard />} />
        <Route exact path="/goals" element={<Goals />} />
        <Route exact path="/progress" element={<Progress />} />
      </Route>
      <Route exact path="/login" element={<Login />} />
      <Route path="*" element={<PageNotFound />} />
    </Routes>
  </BrowserRouter>
);
