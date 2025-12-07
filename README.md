Hotel Management System (FastAPI)
Overview

This is a simple Hotel Management System API made with FastAPI and SQLAlchemy.
It allows you to manage:

Customers
Rooms
Bookings
Payments
Authentication (Login with JWT Token)


Project Structure
hotel_management_system/
│
├── main.py               # App entry point
├── models.py             # Database tables
├── schema.py             # Request & response models
├── database.py           # Database connection
├── basic_auth.py         # JWT auth functions
├── hash.py               # Password hashing
├── login.py              # Login route
├── utils.py              # Load .env settings
│
└── routees/              # API routes
    ├── customers.py
    ├── rooms.py
    ├── bookings.py
    ├── payments.py
    ├── customer_bookings.py
    └── dashboard.py

⚙️ Main Features
✅ Register and login users
✅ Protect routes using JWT (Bearer Token)
✅ CRUD for customers, rooms, bookings, payments
✅ PostgreSQL database
✅ Swagger docs included (/docs)
✅ Passwords are securely hashed

Authentication Flow
Login at /login/ with username and password
Copy the access_token from response
In Swagger → Click Authorize → Paste token → Done
Now you can access protected routes

Requirements:
fastapi
uvicorn
sqlalchemy
psycopg2
pydantic
pydantic-settings
python-jose
python-multipart
passlib[bcrypt]
argon2-cffi
alembic

.env.example
DATABASE CONFIGURATION
# Replace with your actual PostgreSQL connection string
dburi=postgresql://postgres:your_password@localhost:5432/hotel_management_system
secret_key=your_secret_key_here
# JWT encryption algorithm
algorithm=HS256
# Token expiration time (in minutes)
access_token_expire_minutes=60


Author
Muhammad Kashif
Built with using FastAPI and PostgreSQL
