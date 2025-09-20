import React, {useState, useEffect} from 'react';
import { BrowserRouter, Routes, Route, Link } from 'react-router-dom';
import Login from './pages/Login';
import Register from './pages/Register';
import Dashboard from './pages/Dashboard';
import AdminPanel from './pages/AdminPanel';
import jwt_decode from "jwt-decode";

export default function App(){
  const [token, setToken] = useState(localStorage.getItem("token"));
  const [isAdmin, setIsAdmin] = useState(false);

  useEffect(()=>{
    if(token){
      localStorage.setItem("token", token);
      const decoded = jwt_decode(token);
      setIsAdmin(decoded.is_admin);
    }
  },[token]);

  return (
    <BrowserRouter>
      <nav style={{padding:10, borderBottom:"1px solid #ddd"}}>
        <Link to="/">Home</Link> |
        {isAdmin && <Link to="/admin">Admin</Link>} |
        <Link to="/login">Login</Link> |
        <Link to="/register">Register</Link>
      </nav>
      <Routes>
        <Route path="/" element={<Dashboard token={token} />} />
        <Route path="/login" element={<Login setToken={setToken} />} />
        <Route path="/register" element={<Register />} />
        {isAdmin && <Route path="/admin" element={<AdminPanel token={token} />} />}
      </Routes>
    </BrowserRouter>
  )
}


