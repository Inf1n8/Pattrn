import React from "react";
import ReactDOM from "react-dom/client";
import "bootstrap/dist/css/bootstrap.min.css";
import "./index.css";
import App from "./App";
import { BrowserRouter, Route, Routes } from "react-router-dom";
import PageNotFound from "./PageNotFound";
import ProtectedRoute from "./ProtectedRoute";
import Login from "./Login";
import Goals from "./Goals";

const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(
  <BrowserRouter>
    <Routes>
      <Route exact path="/" element={<ProtectedRoute />}>
        <Route exact path="/" element={<App />} />
        <Route exact path="/goals" element={<Goals />} />
      </Route>
      <Route exact path="/login" element={<Login />} />
      <Route path="*" element={<PageNotFound />} />
    </Routes>
  </BrowserRouter>
);
