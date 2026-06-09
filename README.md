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

## 🚀 Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/dottomtundu9-MTUNDU/smart-school-ERP-API
cd school-management-system-API/backend
