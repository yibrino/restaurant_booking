# Restaurant Booking Website

## Overview

The Restaurant Booking Website is a modern web application built using Django and PostgreSQL, which allows customers to create an account and log in to the website. Customers can select a table, date, time, and number of guests for their reservations, ensuring the guest count does not exceed the table's maximum@ capacity. Restaurant owners can manage their bookings, view upcoming reservations, and manage customers through an intuitive admin panel.

## Features

User Authentication: Sign up, log in, and log out.
Table Reservations: Book tables by selecting the desired time slot and the number of guests.
Booking Management: View, edit, and cancel reservations.
Admin Panel: Manage restaurants, tables, reservations, and customers with full CRUD operations.
RESTful API: Access and manage users, tables, and reservations through a comprehensive API.

## Technologies Used

Frontend: HTML, CSS, JavaScript
Backend: Django, Django REST framework
Database: PostgreSQL

## Getting Started

Prerequisites
Python 3.6+
PostgreSQL
Virtual environment tool (e.g., venv)
Heroku CLI (for deployment)

## Installation

1. Clone the repository:
   git clone https://github.com/yourusername/restaurant-booking-website.git
   cd restaurant_booking
2. Set up a virtual environment:

```bash
   python -m bvenv env
```

source env/bin/activate # On Windows use.

```bash
\env\Scripts\activate`
```

3. Install dependencies:

```bash
   pip install -r requirement.txt
```

4. Configure the database:
   Create a PostgreSQL database and update the DATABASES setting in restaurant_booking/settings.py:

   ```bash

   DATABASES = {
   'default': {
   'ENGINE': 'django.db.backends.postgresql',
   'NAME': 'yourdbname',
   'USER': 'yourdbuser',
   'PASSWORD': 'yourdbpassword',
   'HOST': 'localhost',
   'PORT': '5432',
   }
   }
   ```

5. Apply migrations:

```bash
   python manage.py migrate
```

6. Create a superuser:

```bash
   python manage.py createsuperuser
```

7. Run the development server:

```bash
   python manage.py runserver
```

8. Access the application:
   Open your web browser and go to http://127.0.0.1:8000/.

Database Model

```bash

Table admin {
admin_id integer [primary key]
username string
password string
email string
created_at datetime
}

Table tableList {
table_id integer [primary key]
table_name string
admin_id string
number_guests string
created_at datetime
}

Table reservationTable {
reserved_id integer [primary key]
table_id string
table_name string
customer_id integer
date date
time time
number_guests integerss
created_at datetime
}

Table customer {
customer_id integer [primary key]
customer_username string
customer_email string
customer_password password
created_at datetime
}

ref: customer.customer_id < reservationTable.reserved_id
ref: admin.admin_id < tableList.table_id
ref: tableList.table_id < reservationTable.reserved_id

```

Customer Endpoints

```bash
List Customers: GET /api/customers/
Create Customer: POST /ai/customers/create/
Retrieve Customer: GET /api/users/{id}/
Update Customer: PUT /api/customer/update/<int:pk>/
Delete Customer: DELETE /api/customer/<int:pk>/
```

TableList Endpoints

```bash
List Tables: GET /api/tables//
Create Table: POST /api/tables/create/
Retrieve Table: GET /api/table/<int:pk>/
Update Table: PUT /api/tables/update/<int:pk>/
Delete Table: DELETE /api/tables/<int:pk>/
```

Reservation Endpoints

```bash
List Reservations: GET /api/booktables/
Create Reservation: POST /api/booktable/create/
Retrieve Reservation: GET /api/booktable/<int:pk>/
Update Reservation: PUT /api/booktable/update/<int:pk>/
Delete Reservation: DELETE /api/booktable/<int:pk>/
```

Deployment on Heroku

1. Install the Heroku CLI:

2. Log in to Heroku:

3. Create a new Heroku app:
   heroku create your-website-name

4. Add the PostgreSQL add-on:
   heroku addons:create heroku-postgresql:hobby-dev

5. Set up Heroku environment variables:
   heroku config:set DISABLE_COLLECTSTATIC=1

6. Update settings for Heroku:

```bash

Requirements File (requirements.txt)
asgiref==3.8.1
Django==5.0.7
django-cors-headers==4.4.0
djangorestframework==3.15.2
mysqlclient==2.2.4
sqlparse==0.5.1
tzdata==2024.1
psycopg2-binary==2.9.3
```
