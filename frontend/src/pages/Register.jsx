import React, {useState} from 'react';
import API from '../api';

export default function Register(){
  const [n,setN]=useState(""); const [e,setE]=useState(""); const [p,setP]=useState("");
  const submit = async (ev)=>{
    ev.preventDefault();
    await API.post("/api/auth/register", {name:n, email:e, password:p});
    alert("registered, now login");
  };
  return (
    <form onSubmit={submit} style={{maxWidth:400, margin:20}}>
      <h3>Register</h3>
      <input placeholder="name" value={n} onChange={e=>setN(e.target.value)} /><br/>
      <input placeholder="email" value={e} onChange={ev=>setE(ev.target.value)} /><br/>
      <input placeholder="password" type="password" value={p} onChange={ev=>setP(ev.target.value)} /><br/>
      <button type="submit">Register</button>
    </form>
  )
}
