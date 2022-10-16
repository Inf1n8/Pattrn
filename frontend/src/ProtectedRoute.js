import React from "react";
import { Navigate, Outlet } from "react-router-dom";

export default function ProtectedRoute() {
  const isAuthenticated = localStorage.getItem("isAuthenticated");
  return isAuthenticated ? <Outlet /> : <Navigate to="/login" />;
}
