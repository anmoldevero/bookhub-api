# BookHub API

BookHub is a Django REST Framework (DRF) project that provides APIs for managing books and users.  
It supports features like user authentication (JWT), book management, comments, and file uploads (PDFs).

---

## Features
- User authentication (signup, login, logout, change password, delete account)
- Book management (create, list, upload PDFs)
- Search & ordering support 
- Like system for books
- Comment system for books
- JWT token-based authentication
- Media file handling for uploaded files

---

## Authentication
- JWT based login & refresh tokens
- All user actions except signup/login require authentication

---

## API Endpoints (short version)
### User
- `POST /api/users/` → Signup
- `POST /api/token/` → Login (JWT obtain)
- `POST /api/token/refresh/` → Refresh token
- `PUT /api/password/change/` → Change password
- `DELETE /api/users/delete_account/` → Delete account  

### Books
- `POST /api/books/` → Upload new book with PDF
- `GET /api/books/` → List all books
- `POST /api/books/{id}/comment/` → Add comment
- `GET /api/books/{id}/comments/` → Get comments

---

## Setup Instructions
1. Clone the repo:
   ```bash
   git clone <your-repo-link>
Create virtual environment & install dependencies:

bash
Copy code
pip install -r requirements.txt
Run migrations:

bash
Copy code
python manage.py migrate
Start development server:

bash
Copy code
python manage.py runserver
Access API at: http://127.0.0.1:8000/api/

📂 Project Structure
bash
Copy code
bookhub_project/
  ├── books/        # Books app (models, views, serializers)
  ├── users/        # Users app (custom auth logic)
  ├── media/        # Uploaded files (PDFs)
  ├── requirements.txt
  ├── manage.py


# License

MIT License