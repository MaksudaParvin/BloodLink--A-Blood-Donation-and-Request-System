# BloodLink — A Blood Donation & Request System

BloodLink is a Django-based web application developed to address the real-world challenge of finding suitable blood donors quickly during emergencies. It connects donors with people in need through a centralized platform for donor discovery, blood requests, and profile management.

---

## 📌 Project Overview

Finding a suitable blood donor quickly can be difficult during emergencies. BloodLink provides a centralized platform where users can:

- Register and manage their accounts
- Maintain donor information
- Search for donors by blood group and location
- Check donor availability
- View donor profiles
- Create blood requests
- Manage submitted blood requests
- Update request status
- Edit and delete their own requests
- Manage their personal profiles
- Upload profile pictures
- Receive success and error notifications

The system also includes pagination, live location filtering, authentication, ownership restrictions, and responsive UI design.

---

## ✨ Features

### 👤 User Authentication

- User registration
- Email-based login
- Logout functionality
- Password hashing using Django's authentication system
- Custom user model
- Login protection for authenticated features
- Authentication-aware navigation

### 🩸 Donor Management

- Create donor profile during registration
- Blood group information
- Donor location
- Last donation date
- Donor availability
- Donor description
- Profile picture support
- Public donor profile
- Edit donor information
- Delete donor profile
- Ownership-based editing and deletion

### 🔎 Find Blood Donors

Users can search for donors using:

- Blood group
- Location
- Availability

Additional features:

- Live location filtering
- Filter by donor availability
- Clear filters
- Pagination
- Donor result count
- Public donor profile viewing

### 🆘 Blood Requests

Users can create blood requests with:

- Patient name
- Blood group
- Hospital name
- Hospital location
- Required date
- Number of blood bags required
- Contact number
- Description
- Request status

Supported request statuses:

- Pending
- Fulfilled
- Cancelled

### 📋 Request Management

Users can:

- View their blood requests
- View individual request details
- Create new requests
- Edit their own requests
- Delete their own requests
- Update request status
- Filter requests
- View request information

### 👨‍💼 Profile Management

Users can manage:

- Full name
- Email
- Phone number
- Blood group
- Location
- Date of birth
- Profile picture

### 🎨 UI/UX

The interface includes:

- Clean editorial-style design
- Responsive layouts
- Fixed navigation bar
- Fixed footer
- Active navigation states
- Toast notifications
- Delete confirmation modal
- Responsive donor cards
- Responsive filter controls
- Custom CSS without Bootstrap or Tailwind CSS
- Font Awesome icons

---

## 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| Python | Programming language |
| Django | Web framework |
| PostgreSQL | Relational database |
| HTML5 | Page structure |
| CSS3 | Styling and responsive UI |
| JavaScript | Client-side interactions |
| Font Awesome | Icons |
| Pillow | Image processing |
| python-dotenv | Environment variable management |
| psycopg | PostgreSQL database adapter |

---

## 🏗️ Project Structure

```text
BloodLink/
│
├── .env
├── .gitignore
├── manage.py
├── requirements.txt
│
├── config/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── accounts/
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── donors/
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── requests_app/
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── core/
│   ├── __init__.py
│   ├── apps.py
│   ├── urls.py
│   └── views.py
│
├── templates/
│   └── base.html
│
├── static/
│   └── css/
│       ├── base.css
│       ├── accounts/
│       ├── donors/
│       └── requests/
│
└── media/
    └── profile_pictures/
```

---

# ⚙️ Installation & Setup

## 1. Clone the Repository

```bash
git clone https://github.com/MaksudaParvin/BloodLink--A-Blood-Donation-and-Request-System.git
```

Move into the project directory:

```bash
cd "BloodLink--A-Blood-Donation-and-Request-System"
```

---

## 2. Create a Virtual Environment

### Windows

```powershell
python -m venv .venv
```

Activate it:

```powershell
.venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv .venv
```

Activate it:

```bash
source .venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🗄️ PostgreSQL Database Setup

BloodLink uses PostgreSQL instead of SQLite.

Create a PostgreSQL database:

```sql
CREATE DATABASE blood_donate_db;
```

The default configuration uses:

```text
Database: blood_donate_db
User: postgres
Host: localhost
Port: 5432
```

---

# 🔐 Environment Variables

Create a `.env` file in the root directory of the project.

```env
SECRET_KEY=django-insecure-change-this-later
DEBUG=True

DB_NAME=blood_donate_db
DB_USER=postgres
DB_PASSWORD=YOUR_POSTGRES_PASSWORD
DB_HOST=localhost
DB_PORT=5432
```

Replace:

```text
YOUR_POSTGRES_PASSWORD
```

with your actual PostgreSQL password.

---

# 🧪 Database Migrations

After creating or modifying models, run:

```bash
python manage.py makemigrations
```

Then:

```bash
python manage.py migrate
```

---

# 👨‍💻 Create an Admin User

Create a Django superuser:

```bash
python manage.py createsuperuser
```

Enter:

```text
Email
Password
```

---

# ▶️ Running the Project

Activate the virtual environment first.

### Windows

```powershell
.venv\Scripts\activate
```

Then run:

```powershell
python manage.py runserver
```

Open:

```text
http://127.0.0.1:8000/
```

---

# 📜 License

This project is developed for educational and academic purposes.

You may modify and extend the project according to your requirements.

---

# 👩‍💻 Author

**Maksuda Parvin**

BloodLink — Blood Donation & Request Management System

Built with:

```text
Python
Django
PostgreSQL
HTML
CSS
JavaScript
```

---

# ❤️ BloodLink

> **Every drop matters.**

BloodLink aims to make blood donor discovery and blood request management simpler, faster, and more accessible through a centralized web platform.