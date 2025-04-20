# 🌍 Disaster Alert System

A Django-based web application that provides real-time, location-based disaster alerts. Built to help users stay informed and safe during emergencies.

## 🚀 Features

- 🔐 User registration and login  
- 📍 Location-based alert notifications 
- 🛠 Admin dashboard to manage alerts  
- 🧭 Landing page and secure home page  
- 🖥️ Clean, responsive user interface

## 🛠 Tech Stack

- **Backend:** Django (Python)  
- **Frontend:** HTML, CSS, JavaScript  
- **Database:** MySQL

## 🧪 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/AYAScoding/Disaster-Alert-System.git
   cd disaster-alert-system
2. **Set up and activate a virtual environment**
   ```bash
    python -m venv env
    source env/bin/activate  # On Windows: env\Scripts\activate

3. **Install dependencies**
    ```bash
    pip install -r requirements.txt

4. **Run migrations**
    ```bash
   python manage.py migrate

6. **Start the development server**
    ```bash
    python manage.py runserver


📌 Notes:

Only superusers (admins) can create and manage alerts.

Users receive alerts based on their selected location during registration.
