import React, {useState} from 'react';
import API, { setAuthToken } from '../api';
import { useNavigate } from 'react-router-dom';

export default function Login({ setToken }){
  const [email,setEmail]=useState("");
  const [password,setPassword]=useState("");
  const nav = useNavigate();

  const submit = async (e)=>{
    e.preventDefault();
    const res = await API.post("/api/auth/login", {email, password});
    const token = res.data.access_token;
    setToken(token);
    setAuthToken(token);
    nav("/");
  };

  return (
    <form onSubmit={submit} style={{maxWidth:400, margin:20}}>
      <h3>Login</h3>
      <input placeholder="email" value={email} onChange={e=>setEmail(e.target.value)} /><br/>
      <input placeholder="password" type="password" value={password} onChange={e=>setPassword(e.target.value)} /><br/>
      <button type="submit">Login</button>
    </form>
  )
}
