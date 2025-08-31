# Telecom ERP API - ALX Capstone Project

A comprehensive **Django REST Framework** backend for telecommunications operations management.  
This ERP system provides **role-based access control** for managing users, departments, tasks, operations, and approvals with secure file upload capabilities.

---

## 🚀 Features

### ✅ Implemented in V1
- **JWT Authentication** – Secure login/logout/refresh endpoints  
- **Role-Based Access Control** – Admin, Manager, Engineer, Staff permissions  
- **Department Management** – Create and organize teams  
- **Task Management** – Assign and track tasks with status workflows  
- **Operations Workflow** – Engineers report work, managers approve  
- **File Uploads** – Image evidence for operations  
- **Approval System** – Multi-status workflow with comments  
- **RESTful API** – Complete CRUD operations with permissions  
- **Swagger Documentation** – Interactive API documentation  

---

## 📋 Role Permissions

- **Admins:** Full system access  
- **Managers:** Department management, operation approvals  
- **Engineers:** Task execution, operation reporting, file uploads  
- **Staff:** Limited view access  

---

## 🛠️ Tech Stack

- **Backend:** Django 4.2 + Django REST Framework  
- **Database:** MySQL  
- **Authentication:** JWT (SimpleJWT)  
- **File Storage:** Django Media Files  
- **API Documentation:** drf-spectacular (Swagger/OpenAPI)  
- **Validation:** Django model and serializer validation  

---

## 📦 Installation

```bash
# 1. Clone repository
git clone <your-repo-url>
cd telecom_erp_api

# 2. Create virtual environment
python -m venv .venv
source .venv/bin/activate  # macOS/Linux
# .venv\Scripts\activate   # Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Environment setup
cp .env.example .env
# Edit .env with your database and secret key

# 5. Run migrations
python manage.py migrate

# 6. Create superuser
python manage.py createsuperuser

# 7. Run server
python manage.py runserver
