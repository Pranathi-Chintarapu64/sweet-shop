import React, {useState, useEffect} from 'react';
import API, { setAuthToken } from '../api';

export default function AdminPanel({ token }){
  const [name,setName]=useState(""); const [cat,setCat]=useState(""); const [price,setPrice]=useState(1); const [qty,setQty]=useState(1);
  const [sweets, setSweets] = useState([]);

  useEffect(()=>{
    if(token) setAuthToken(token);
    fetchSweets();
  },[token]);

  async function fetchSweets(){ const r = await API.get("/api/sweets"); setSweets(r.data); }
  async function add(e){ e.preventDefault(); await API.post("/api/sweets", {name, category:cat, price, quantity:qty}); fetchSweets(); }
  async function deleteSweet(id){ await API.delete(`/api/sweets/${id}`); fetchSweets(); }
  async function restock(id){ const amount = 5; await API.post(`/api/sweets/${id}/restock`, {quantity:amount}); fetchSweets(); }

  return (
    <div style={{padding:20}}>
      <h3>Admin Panel</h3>
      <form onSubmit={add}>
        <input placeholder="name" value={name} onChange={e=>setName(e.target.value)} /><br/>
        <input placeholder="category" value={cat} onChange={e=>setCat(e.target.value)} /><br/>
        <input placeholder="price" value={price} onChange={e=>setPrice(e.target.value)} type="number" /><br/>
        <input placeholder="qty" value={qty} onChange={e=>setQty(e.target.value)} type="number" /><br/>
        <button type="submit">Add Sweet</button>
      </form>
      <hr/>
      <h4>Existing</h4>
      {sweets.map(s => (
        <div key={s.id} style={{border:"1px solid #ddd", padding:8, marginBottom:6}}>
          {s.name} — {s.quantity}
          <button onClick={()=>restock(s.id)} style={{marginLeft:8}}>Restock +5</button>
          <button onClick={()=>deleteSweet(s.id)} style={{marginLeft:8}}>Delete</button>
        </div>
      ))}
    </div>
  );
}
