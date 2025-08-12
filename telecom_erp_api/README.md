# Telecom ERP Backend

A Django REST Framework-powered backend for managing operations in a telecommunication company.  
This ERP system provides tools for managing users, roles, permissions, departments, tasks, approvals, file uploads, and activity logs.

## Features

- **User Authentication & Roles**  
  - Secure JWT & Token authentication  
  - Role-based access control (Admin, Manager, Employee)  
  - Custom permissions per department and task level  

- **Department Management**  
  - Create, update, and delete departments  
  - Assign users to departments  

- **Task Management**  
  - Create tasks and assign them to users  
  - Track task progress and completion  
  - Add comments and deadlines  

- **Approval Workflow**  
  - Multi-level approval process for tasks/projects  
  - Approve or reject requests with comments  

- **File & Media Uploads**  
  - Upload images, documents, and signatures  
  - Link uploads to tasks or approvals  

Future feature
- **Activity Logs**  
  - Track all actions performed in the system  
  - Store timestamps, actors, and affected entities  

---

## Tech Stack

- **Backend:** Django, Django REST Framework  
- **Authentication:** JWT (SimpleJWT) & Token Auth  
- **Database:** PostgreSQL (recommended)  
- **Storage:** Local or AWS S3 for file uploads  
- **Testing:** Django Test Framework, DRF API TestCase  
- **Documentation:** DRF's built-in API docs + Swagger (drf-yasg)

---

## Project Structure

```plaintext
telecom_erp_backend/
│
├── accounts/       # Authentication, roles, permissions
├── departments/    # Department CRUD
├── tasks/          # Task management
├── approvals/      # Approval workflows
├── uploads/        # File uploads
├── telecom_erp_backend/  # Project settings & URLs
└── manage.py


## Installation
1️. Clone the repository
bash
git clone https://github.com/<your-username>/telecom-erp-backend.git
cd telecom-erp-backend

2️. Create a virtual environment
Bash
python -m venv .venv
source .venv/bin/activate  # On macOS/Linux
.venv\Scripts\activate     # On Windows

3️. Install dependencies
bash
pip install -r requirements.txt

4️. Set up environment variables
Create a .env file in the root folder:
env
SECRET_KEY=your_secret_key
DEBUG=True
DATABASE_URL=postgres://user:password@localhost:5432/telecom_erp
ALLOWED_HOSTS=127.0.0.1,localhost

5️. Run migrations
bash
python manage.py migrate

6️. Create a superuser
bash
python manage.py createsuperuser

7️. Start the development server
bash
python manage.py runserver


API Endpoints Documentation

Method: POST
Endpoint: /api/auth/login/
Description: Login and get token

Method: POST
Endpoint: /api/auth/register/
Description: Register new user

Method: GET
Endpoint: /api/departments/
Description: List departments

Method: POST
Endpoint: /api/departments/
Description: Create department

Method: GET
Endpoint: /api/tasks/
Description: List tasks

Method: POST
Endpoint: /api/tasks/
Description: Create task

Method: PATCH
Endpoint: /api/tasks/{id}/
Description: Update task

Method: POST
Endpoint: /api/approvals/
Description: Submit approval

Method: POST
Endpoint: /api/uploads/
Description: Upload file

<!-- 🧪 Running Tests
python manage.py test -->


## License
This project is licensed under the MIT License.

## Contributing
Pull requests are welcome, For major changes, please open an issue first to discuss what you would like to change.

## Author
Ibrahim Sakariyah Temitope (Topzee) – Backend Developer
GitHub: @topzee001 LinkedIn: Ibrahim Sakariyah
