import axios from "axios";

const API = axios.create({
  baseURL: import.meta.env.VITE_API_BASE || "http://localhost:8000"
});

export function setAuthToken(token){
  API.defaults.headers.common["Authorization"] = `Bearer ${token}`;
}

export default API;
