# 🏡 Real Estate Management System

A web-based Real Estate Management System developed using Python, Django, and MySQL. This project helps manage properties, agents, clients, property inquiries, and property tour bookings.

## 🚀 Features

- Dashboard with property, inquiry, and tour statistics.
- View and search available properties.
- Filter properties by type and status.
- View complete property details.
- Submit property inquiries.
- Schedule property tours.
- Validate tour booking date and time.
- Manage properties, agents, clients, inquiries, and tours through Django Admin.
- MySQL database integration.
- Responsive website interface.

## 🛠️ Technologies Used

- Python
- Django
- MySQL
- HTML
- CSS
- JavaScript
- Django Admin

## 📁 Project Structure

```text
RealEstateProject/
├── properties/
│   ├── migrations/
│   ├── templates/
│   │   └── properties/
│   │       ├── base.html
│   │       ├── dashboard.html
│   │       ├── property_list.html
│   │       └── property_detail.html
│   ├── admin.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
├── realestate/
│   ├── settings.py
│   └── urls.py
├── manage.py
├── requirements.txt
└── README.md