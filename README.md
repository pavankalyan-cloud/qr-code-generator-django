# QR Code Generator Web Application

![Python](https://img.shields.io/badge/Python-3.12-blue)
![Django](https://img.shields.io/badge/Django-5.x-green)
![DRF](https://img.shields.io/badge/Django%20REST%20Framework-red)
![MySQL](https://img.shields.io/badge/MySQL-Database-orange)
![GitHub](https://img.shields.io/badge/GitHub-Repository-black)

A full-stack QR Code Generator built using **Django**, **Django REST Framework**, **MySQL**, and a **React frontend**.

---

## Features

- User Registration
- User Login (JWT Authentication)
- Generate QR Codes
- Download QR Codes
- QR History
- Pagination
- REST APIs
- MySQL Database Support

---

## Tech Stack

### Backend
- Python
- Django
- Django REST Framework
- MySQL

### Frontend
- React
- Vite
- Axios
- React Router

---

## Project Structure

```
apiapp/
qrapp/
qrproject/
manage.py
```

---

## Installation

### Clone

```bash
git clone https://github.com/pavankalyan-cloud/qr-code-generator-django.git
```

### Install

```bash
pip install -r requirements.txt
```

### Run

```bash
python manage.py migrate
python manage.py runserver
```

---

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | /api/register/ | Register user |
| POST | /api/login/ | Login |
| POST | /api/generate/ | Generate QR |
| GET | /api/history/ | QR History |

---

## React Frontend

Frontend Repository:

https://github.com/pavankalyan-cloud/qr-code-generator-react

---

## Future Improvements

- Deploy Backend on Render
- Deploy Frontend on Vercel
- Dark Mode
- QR Customization
- User Dashboard

---

## Author

**Pavan Kalyan**
