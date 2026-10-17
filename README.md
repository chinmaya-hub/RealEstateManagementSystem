# 🏡 Real Estate Management System

A web-based Real Estate Management System developed using **Python, Django, and MySQL**. This application provides a centralized platform to manage properties, real estate agents, clients, property inquiries, and property tour bookings through a user-friendly web interface.

## 📌 Project Overview

The Real Estate Management System simplifies common real estate management operations by providing property listings, detailed property information, inquiry submission, tour scheduling, and administrative management.

The project uses Django for backend development and MySQL for database management.

## 🚀 Features

### 🏠 Property Management
- View available property listings.
- Search and filter properties.
- Filter properties by property type and status.
- View complete property details.
- Upload and display property images.
- Manage property records through Django Admin.

### 📊 Dashboard
- Dashboard displaying property statistics.
- Overview of property inquiries.
- Property tour statistics.
- Centralized access to important information.

### 👥 Agent Management
- Manage real estate agent records.
- Add, view, update, and delete agents.

### 🤝 Client Management
- Maintain client information.
- Add, view, update, and delete client records.

### 📩 Property Inquiries
- Submit inquiries about properties.
- Store inquiry information in the database.
- Manage inquiries through Django Admin.

### 📅 Property Tour Booking
- Schedule property tours.
- Validate tour booking dates and times.
- Store tour booking information.
- Manage tour records through Django Admin.

### 🔐 Administration
- Django Admin integration.
- Centralized management of properties, agents, clients, inquiries, and tours.

### 📱 Responsive Interface
- User-friendly website interface.
- Responsive layouts for desktop and mobile devices.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Backend programming |
| Django | Web framework |
| MySQL | Relational database |
| HTML5 | Website structure |
| CSS3 | Styling and responsive layouts |
| JavaScript | Frontend interactions |
| Django Admin | Administrative management |
| Git | Version control |
| GitHub | Source code hosting |

## 📁 Project Structure

```text
RealEstateProject/
│
├── properties/
│   ├── migrations/
│   ├── templates/
│   │   └── properties/
│   │       ├── base.html
│   │       ├── dashboard.html
│   │       ├── property_list.html
│   │       ├── property_detail.html
│   │       ├── agent_list.html
│   │       ├── agent_form.html
│   │       ├── agent_confirm_delete.html
│   │       ├── client_list.html
│   │       ├── client_form.html
│   │       └── client_confirm_delete.html
│   │
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
├── realestate/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── .gitignore
├── database.sql
├── manage.py
├── README.md
└── requirements.txt