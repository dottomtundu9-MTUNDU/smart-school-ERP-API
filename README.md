# smart-school-ERP-API

# SmartSchool ERP API 🚀

A robust, enterprise-grade School Management System API built with **FastAPI**, **SQLAlchemy**, and **PostgreSQL**. Designed to automate school operations, financial tracking, student grading, and role-based access control.

---

## ✨ Features

- **Advanced Authentication:** Secure login using JWT (JSON Web Tokens) with OAuth2.
- **Role-Based Access Control (RBAC):** Distinct permissions for `SuperAdmin`, `Admin`, `Teacher`, `Accountant`, and `Student`.
- **Student Lifecycle Management:** Complete CRUD for student registration, classes, and promotions.
- **Financial & Fee Management (Monetization Core):** Invoice generation, fee payment tracking, and balance statements.
- **Highly Scalable Architecture:** Strictly follows the Service-Repository pattern for easy maintenance.

---

## 🛠️ Tech Stack

- **Framework:** FastAPI (Python 3.10+)
- **Database ORM:** SQLAlchemy v2.0
- **Database:** PostgreSQL (Production) / SQLite (Development)
- **Data Validation:** Pydantic v2
- **Security:** Passlib (bcrypt) & PyJWT

---
backend/
│
├── app/
│   ├── __init__.py
│   ├── main.py                  # Mlango mkuu wa API (FastAPI instance & middleware)
│   │
│   ├── core/                    # Mipangilio mikuu ya mfumo
│   │   ├── __init__.py
│   │   ├── config.py            # Inasoma .env (Mazingira ya siri)
│   │   ├── security.py          # Hash za password na JWT tokens
│   │   └── database.py          # SQLAlchemy engine na Session ya DB
│   │
│   ├── models/                  # Database Tables (SQLAlchemy Models)
│   │   ├── __init__.py
│   │   ├── user.py              # Walimu, Wanafunzi, Ma-admin
│   │   ├── student.py           # Taarifa za wanafunzi
│   │   └── finance.py           # Malipo ya ada na ankara (Invoices)
│   │
│   ├── schemas/                 # Pydantic Models (Validations za data zinazoingia/toka)
│   │   ├── __init__.py
│   │   ├── user.py
│   │   ├── student.py
│   │   └── finance.py
│   │
│   ├── routers/                 # API Endpoints (Controllers)
│   │   ├── __init__.py
│   │   ├── auth.py              # Login na kupewa Token
│   │   ├── students.py          # CRUD ya wanafunzi
│   │   └── finance.py           # CRUD ya ada na malipo
│   │
│   └── services/                # Business Logic (Hapa ndio akili ya mfumo ilipo)
│       ├── __init__.py
│       ├── student_service.py
│       └── finance_service.py
│
├── .env                         # Faili la siri (Database URL, Secret Keys)
├── .gitignore                   # Kuzuia faili zisizoenda GitHub (kama .env au venv)
├── requirements.txt             # Maktaba zote za Python zinazohitajika
└── README.md                    # Maelezo ya mradi kwa wateja/wawekezaji

## 🚀 Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/dottomtundu9-MTUNDU/smart-school-ERP-API
cd school-management-system-API/backend
