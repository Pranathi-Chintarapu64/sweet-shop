# Sweet Shop Management System

## Project Overview

This project is a **full-stack Sweet Shop Management System** that allows users to browse and purchase sweets, while admins can manage inventory (add, update, delete, restock sweets).  

The backend is built with **FastAPI** and uses **SQLite** (can be switched to PostgreSQL). The frontend is a minimal **React SPA** built with Vite. The project demonstrates **TDD principles**, clean architecture, and AI-assisted development.

---

## Tech Stack

| Layer          | Technology                       |
|----------------|----------------------------------|
| Backend        | Python, FastAPI                  |
| Database       | SQLite (default)                 |
| Authentication | JWT via PyJWT                     |
| Frontend       | React + Vite                     |
| HTTP Client    | Axios                             |
| Styling        | Minimal CSS                      |
| Testing        | pytest, httpx, pytest-asyncio    |
| Version Control| Git + GitHub                     |

---

## Backend API Endpoints

### Auth
- `POST /api/auth/register` — Register a new user.
- `POST /api/auth/login` — Login and receive a JWT token.

### Sweets (Protected — requires token)
- `POST /api/sweets` — Add a new sweet.
- `GET /api/sweets` — List all sweets.
- `GET /api/sweets/search` — Search sweets by name, category, price range.
- `PUT /api/sweets/{id}` — Update a sweet’s details.
- `DELETE /api/sweets/{id}` — Delete a sweet (Admin only).

### Inventory (Protected)
- `POST /api/sweets/{id}/purchase` — Purchase a sweet (reduces quantity).
- `POST /api/sweets/{id}/restock` — Restock a sweet (Admin only).

**Authentication:** Use `Authorization: Bearer <token>` header for protected routes.

---

## Frontend Functionality

- User registration and login.
- Dashboard displays all sweets, with purchase buttons (disabled if quantity = 0).
- Admin panel:
  - Add new sweets
  - Restock existing sweets
  - Delete sweets
- Minimal responsive design using CSS grid and simple forms.

---

## Project Setup

### Backend

1. Clone the repo:
```bash
git clone https://github.com/<your-username>/sweet-shop.git
cd sweet-shop/backend
```
```bash
Install dependencies:
python -m venv .venv
activate venv
pip install -r requirements.txt
```
```bash
run code:
uvicorn app.main:app --reload
Runs on http://localhost:8000.
```

###Frontend
Navigate to frontend folder:

```bash
cd ../frontend
```
```bash
Install dependencies:
npm install

Start dev server:
npm run dev
```

Open browser:
http://localhost:5173
Frontend communicates with backend at http://localhost:8000 by default.

###Running Tests
```bash
cd backend
pytest
```
Includes tests for authentication (test_auth.py) and sweets CRUD & inventory operations (test_sweets.py).

### Screenshots 

Swagger UI with endpoints- 
[!swagger ui] (1.png)

[!swagger ui] (2.png)


---

##My AI Usage
I used ChatGPT to assist with:

- Generating boilerplate code for FastAPI routers and Pydantic schemas.
- Suggesting initial React components for Dashboard and AdminPanel.
- Drafting test cases in pytest for TDD.
- Debugging JWT authentication and API integration.

Impact: AI accelerated setup and allowed me to focus on custom business logic, UI design, and testing. Every suggestion was reviewed and adjusted manually.
