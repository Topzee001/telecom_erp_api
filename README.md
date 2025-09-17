# Telecom ERP API - ALX Capstone Project

A comprehensive **Django REST Framework** backend for telecommunications operations management.  
This ERP system provides **role-based access control** for managing users, departments, tasks, operations, and approvals with secure file upload capabilities.

---

## Features

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

## Role Permissions

- **Admins:** Full system access  
- **Managers:** Department management, operation approvals  
- **Engineers:** Task execution, operation reporting, file uploads  
- **Staff:** Limited view access  

---

## Tech Stack

- **Backend:** Django 4.2 + Django REST Framework  
- **Database:** MySQL  
- **Authentication:** JWT (SimpleJWT)  
- **File Storage:** Django Media Files  
- **API Documentation:** drf-spectacular (Swagger/OpenAPI)  
- **Validation:** Django model and serializer validation  

---

## Installation

```bash
# 1. Clone repository
git clone https://github.com/Topzee001/telecom_erp_api.git
cd telecom_erp_api

# 2. Create virtual environment
python -m venv .venv
source .venv/bin/activate  # macOS/Linux
# .venv\Scripts\activate   # Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Environment setup
cp .env.example .env
# Edit .env with your database URL and secret key

# 5. Run migrations
python manage.py migrate

# 6. Create superuser
python manage.py createsuperuser

# 7. Run server
python manage.py runserver
```
## API Endpoints

### Authentication
- `POST /api/accounts/login/` – JWT login  
- `POST /api/accounts/register/` – User registration  
- `POST /api/accounts/logout/` – JWT logout  
- `POST /api/accounts/refresh/` – Token refresh  

### Users & Profiles
- `GET /api/accounts/me/` – Current user profile  
- `GET /api/accounts/users/` – List users (Admin)  
- `GET/PUT /api/accounts/users/details/{id}/` – User details  

### Departments
- `GET/POST /api/departments/` – List/create departments  
- `GET/PUT/DELETE /api/departments/{id}/` – Department CRUD  

### Tasks
- `GET/POST /api/tasks/` – List/create tasks  
- `GET /api/tasks/my-tasks/` – User's assigned tasks  
- `PATCH /api/tasks/status/{id}/` – Update task status  
- `GET /api/tasks/summary/` – Task statistics (Admin/Manager)  

### Operations
- `GET/POST /api/operations/` – List/create operations  
- `PATCH /api/operations/approvals/{id}/` – Approve/reject operations  
- `GET /api/operations/summary/` – Operation statistics  

### Uploads
- `POST /api/uploads/` – Upload operation images  

---

## Usage Examples

### Engineer Workflow
1. Login with engineer credentials  
2. View assigned tasks → `GET /api/tasks/my-tasks/`  
3. Create operation report → `POST /api/operations/`  
4. Upload evidence images → `POST /api/uploads/`  

### Manager Workflow
1. Login with manager credentials  
2. Review pending operations → `GET /api/operations/`  
3. Approve/Reject with comments → `PATCH /api/operations/approvals/{id}/`  
4. View department statistics → `GET /api/tasks/summary/`  

---

## 📊 Database Schema
- **User** → Department (FK)  
- **Task** → Department (FK), User (FK)  
- **Operation** → Task (FK), User (FK)  
- **Upload** → Operation (FK), User (FK)  

---

## Security Features
- ✅ JWT token authentication with blacklisting  
- ✅ Role-based permission classes  
- ✅ Object-level access control  
- ✅ Input validation and sanitization  
- ✅ Secure file upload handling  

---

## Testing

```bash
# Run all tests
python manage.py test

# Run tests for a specific app
python manage.py test accounts.tests
```
## API Documentation
Interactive Swagger documentation is available at:
[Documentation](https://telecom-erp-api.onrender.com/api/swagger/)

## Deployment

##Production Setup

1. Set DEBUG=False in environment variables
2. Configure production database (MySQL/PostgreSQL)
3. Set up static file serving (Whitenoise/Nginx)
4. Configure media file storage (AWS S3 recommended)
5. Set up WSGI server (Gunicorn + Nginx)
   
## Environment Variables
```
DEBUG=False
SECRET_KEY=your-production-secret-key
DATABASE_URL=mysql://user:password@host:port/database
ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com
```

## Contributing
1. Fork the repository
2. Create feature branch → git checkout -b feature/amazing-feature
3. Commit changes → git commit -m 'Add amazing feature'
4. Push to branch → git push origin feature/amazing-feature
5. Open a Pull Request
   
## License
This project is licensed under the MIT License – see the LICENSE file for details.

## Author
Ibrahim Sakariyah Temitope (Topzee)
GitHub: @topzee001
LinkedIn: Ibrahim Sakariyah

## ALX Software Engineering Program
🎓 ALX Capstone Project
This project was developed as the Capstone Project for the ALX Software Engineering program, demonstrating proficiency in:
- Django REST Framework
- Database design
- Authentication systems
- API development
