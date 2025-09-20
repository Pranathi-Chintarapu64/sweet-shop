import React, {useState, useEffect} from 'react';
import API, { setAuthToken } from '../api';

export default function Dashboard({ token }){
  const [sweets, setSweets] = useState([]);
  useEffect(()=>{
    if(token) setAuthToken(token);
    fetchSweets();
  },[token]);

  async function fetchSweets(){
    const res = await API.get("/api/sweets");
    setSweets(res.data);
  }

  async function purchase(id){
    const qty = 1;
    await API.post(`/api/sweets/${id}/purchase`, { quantity: qty });
    fetchSweets();
  }

  return (
    <div style={{padding:20}}>
      <h2>Available Sweets</h2>
      <div style={{display:"grid", gridTemplateColumns:"repeat(auto-fit, minmax(220px, 1fr))", gap:10}}>
        {sweets.map(s => (
          <div key={s.id} style={{border:"1px solid #ccc", padding:10}}>
            <h4>{s.name}</h4>
            <div>Category: {s.category}</div>
            <div>Price: {s.price}</div>
            <div>Qty: {s.quantity}</div>
            <button disabled={s.quantity === 0} onClick={()=>purchase(s.id)}>Purchase</button>
          </div>
        ))}
      </div>
    </div>
  )
}
