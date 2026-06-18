# QR Code Generator Web Application

![Python](https://img.shields.io/badge/Python-3.12-blue)
![Django](https://img.shields.io/badge/Django-5.x-green)
![Django REST Framework](https://img.shields.io/badge/DRF-REST_API-red)
![MySQL](https://img.shields.io/badge/MySQL-Database-orange)
![GitHub](https://img.shields.io/badge/GitHub-Repository-black)

A full-stack QR Code Generator Web Application built using **Django**, **Python**, **MySQL**, and **Django REST Framework**. The application allows users to register, generate QR codes instantly, and provides REST APIs for QR code generation.

---

## Features

- User Registration
- QR Code Generation
- Django REST Framework APIs
- MySQL Database Integration
- Responsive User Interface
- Instant QR Code Preview
- Base64 QR Generation (No unnecessary image storage)
- Clean and Modular Django Project Structure

---

## Tech Stack

### Backend
- Python
- Django
- Django REST Framework

### Database
- MySQL

### Frontend
- HTML
- CSS
- JavaScript

### Tools
- Git
- GitHub
- VS Code

---

## Project Structure

```
QRPROJECT/
│
├── apiapp/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   └── urls.py
│
├── qrapp/
│   ├── migrations/
│   ├── static/
│   ├── templates/
│   ├── views.py
│   ├── models.py
│   └── urls.py
│
├── qrproject/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── manage.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Installation

### Clone the Repository

```bash
git clone https://github.com/pavankalyan-cloud/qr-code-generator-django.git

cd qr-code-generator-django
```

---

### Create Virtual Environment

```bash
python -m venv venv
```

---

### Activate Virtual Environment

Windows

```bash
venv\Scripts\activate
```

Linux/macOS

```bash
source venv/bin/activate
```

---

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

### Configure Database

Update your MySQL database credentials inside **settings.py**.

Example:

```python
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "your_database_name",
        "USER": "your_username",
        "PASSWORD": "your_password",
        "HOST": "localhost",
        "PORT": "3306",
    }
}
```

---

### Apply Migrations

```bash
python manage.py makemigrations

python manage.py migrate
```

---

### Run the Server

```bash
python manage.py runserver
```

Visit:

```
http://127.0.0.1:8000/
```

---

## REST API

Example API endpoint:

```
GET /api/
```

Depending on your implementation, additional endpoints may be available for QR code generation.

---

## How It Works

1. User enters text or a URL.
2. Django processes the request.
3. The QR Code library generates the QR image.
4. The image is converted into Base64 format.
5. The Base64 image is displayed instantly in the browser.
6. No QR image files are stored on the server.

---

## Future Enhancements

- JWT Authentication
- Download QR Code
- QR Code History
- Custom QR Colors
- QR Analytics Dashboard
- Docker Support
- AWS Deployment
- Render Deployment

---

## Author

**Pavan Kalyan Gorrela**

GitHub:
https://github.com/pavankalyan-cloud

LinkedIn:
(Add your LinkedIn profile here)

---

## License

This project is created for learning, portfolio, and interview demonstration purposes.
