# Restaurant Booking Website

The Restaurant Booking Website is a restaurant website that enables customers to book a table online.
People who would like to book a table online in a restaurant would benefit from using this website.

![Screenshot demonstrating website responsiveness](/assets/readme_image/website_responsiveness.jpg)

## List of links
- [GitHub Repo](https://github.com/ROCK3879/restaurant_booking_1)
- [Live Link](https://restaurant-booking-no1-ae7b2991e60d.herokuapp.com/)
- [BACKLOG link](https://github.com/users/ROCK3879/projects/4/views/1)


# Overview

The Restaurant Booking Website is a web application built using Django and PostgreSQL, which allows customers to create an account and log in to the website. Customers can select a table, date, time, and number of guests for their reservations, ensuring the guest count does not exceed the table's maximum capacity. Restaurant owners can manage their bookings, view upcoming reservations, and manage customers through an intuitive admin panel.


# User stories

## Admin wants to view all bookings

As an admin, I want to view all bookings so that I can manage the restaurant’s reservations.

## Admin wants to prevent a double bookings

As an admin, I can prevent a double booking so that I can guarantee that a table can't be booked twice for the same date and time.

## User wants to view the restaurant menu

As a user, I want to view the restaurant menu so that I can see what food options are available.

## User wants to book a table for a specific date and time

As a user, I want to book a table for a specific date and time so that I can plan my visit to the restaurant.

## User wants to specify the number of guests for their booking

As a user, I want to specify the number of guests for my booking so that the restaurant can prepare the necessary meals and seating.

## User wants to receive a confirmation message as soon as they book a table

As a user, I want to receive a confirmation message after booking a table so that I know my booking has been successfully recorded.

## User wants to be able to cancel their booking

As a user, I want to be able to cancel my booking so that I can change my plans if necessary.

## User wants to be able to update a booking

As a user, I want to update any of my bookings so that I my updated booking will suit my new needs and circumstances.

## User wants to register on the restaurant website

As a user, I can register on the restaurant website so that I can sign in to my account.

## User wants to sign in to their account on the restaurant website

As a user, I can sign in to my account on the restaurant website so that I can book a table.

## User wants to sign out of their account on the restaurant website

As a user, I can sign out of my account on the restaurant website so that I my account stays safe.


# Features

User Authentication: Sign up, log in, and log out.
Table Reservations: Book tables by selecting the desired time slot and the number of guests.
Booking Management: View, edit, and cancel reservations.
Admin Panel: Manage restaurants, tables, reservations, and customers with full CRUD operations.
RESTful API: Access and manage users, tables, and reservations through a comprehensive API.


## Navigation bar

The fully responsive navigation bar is featured on all pages, includes links to each of the home, gallery, menu, contact pages and register, sign in, my booking, sign out, and book a table forms and is identical on each page to allow for easy navigation.
This section will allow a user to easily navigate from page to page.

![Navigation bar](/assets/readme_image/navigation_bar.jpg)


## Home page

The home page shows a close-up of a part of the restaurant with a blurry background and inscription "Welcome to Restaurant No1"
"Experience the finest dining with us".
Button: Log In, allows the user to access his account and the possibilities of booking a table, update and cancel.
"Register for exculusive offers" 
Button: Register Now,enables new users to register and after registration have the possibility of booking, updating and canceling a reservation.
Below are screenshot of the home page.

![Home page](/assets/readme_image/home_page.jpg)


## Gallery page

This gallery page changes the about us section because a picture speaks louder than words. Here there is a possibility to expand the gallery with additional images as needed.
It tells a user about "Restaurant No1" is a family-owned restaurant in Germany that offers its customers various, tasty, healthy meals and drinks.
Additionally, it emphasizes that a customer can easily book a table online as soon as they will have registered on the restaurant website.
Below are screenshot of the "Gallery".

![Gallery page 1](/assets/readme_image/gallery_page_1.jpg)

![Gallery page 2](/assets/readme_image/gallery_page_2.jpg)

![Gallery page 3](/assets/readme_image/gallery_page_3.jpg)


## Menu

The restaurant menu exist on the menu page.
It contains only 8 items, each has an image. The menu is presented with couple options and has the possibility to increase the offer if necessary.
All meals and drinks images are fully responsive on all screen sizes.
Below are screenshot of the restaurant menu.

![Menu page](/assets/readme_image/menu_page.jpg)


## Contact page

The restaurant contact form exist on the navigation bar.
It contains 3 field and 1 submit button. The contact form is presented with fields: Name, Email, Message through this form, the user can get in touch with the restaurant staff if they have additional questions.
Below are screenshot of the restaurant contact page.

![Contact page empty](/assets/readme_image/contact_page_empty.jpg)

![Contact page full](/assets/readme_image/contact_page_full.jpg)

![Contact page with error](/assets/readme_image/contact_page_with_error.jpg)


## Register

On the register page, there is a register form that enables a customer to register by entering a username, an email, and a password.
A user must confirm their password.
The register form examines the right formula of an email. If its formula was not correct, an error message will appear.
As a user enters their password, and user confirms their password, the two must be identical. If they are not, an error message will become visible.
Below are eight screenshots of the register form.

![Register customer error password not match](/assets/readme_image/register_customer_error_password_not_match.jpg)

![Register customer error email](/assets/readme_image/register_customer_error_email.jpg)


## Login

A Login button exists on the home page.
To login, a registered user must enter their username and password.
A registered user must enter a valid username and password, if either a username or a password is not valid, an error message arises.
As a user successfully signs in, a confirmation message materializes, and the user can go into the booking page to be able to book a restaurant table.
Beneath are screenshots that demonstrate the sign-in form.

![Login customer username or password not valid](/assets/readme_image/login_customer_username_or_password_not_valid.jpg)

![Login customer](/assets/readme_image/login_customer.jpg)


## Book a table

The New Booking, My booking and Logout button appears on the nav bar only after a user will have Login.
A logedin user can book a table in restaurant by means of a booking form that is built in the "New Booking" page.
To book a table, a user should choose a certain table for a specific date and time, the user should also choose a certain number of guests.
If the table, date, and time that a user chooses are already booked, an error message appears and encourages the user to choose another table, date, or time to be able to book a table.
If a user chooses a number of guests that is not compatible with the capacity of the table that the user wants to book, an error message pops up and notifies the user about that.
As a user successfully books a table, a confirmation message informs the user about that.
Underneath are screenshots that illustrate the details of signing in above. 

![Booking new booking customer](/assets/readme_image/new_booking_customer.jpg)

![Booking new booking customer alert already booked](/assets/readme_image/new_booking_customer_alert_already_booked.jpg)

![Booking new booking customer alert number of guests not allowed](/assets/readme_image/new_booking_customer_alert_number_of_guests_not_allowed.jpg)

![Booking new booking customer alert alrady booked for this date](/assets/readme_image/new_booking_customer_alert_alrady_booked_for_this_date.jpg)

![Booking new booking customer alert booked successfully](/assets/readme_image/new_booking_customer_alert_booked_successfully.jpg)


## My Bookings

The My Bookings button appears on the same nav bar as New Booking and Logout button after a user will have signed in.
Clicking on My Bookings will open the My Bookings table on the website.
On My Bookings page, a Logedin user can see their list of bookings, update them, cancel them or logout.
On each booking, there are all the details of that booking, to the right there are two buttons: Edit and Cancel.
If a user clicks inside a certain booking on the Edit button, a form for updating a booking opens up prepopulated with the settings of the booking that the customer wants to update. The user can choose new settings to be applied for that booking if these are available, that booking will be updated and the user can see into their My Bookings table, where they can find their updated booking. If these are not available, however, an error message arises, tells the user that those settings are already booked, and urges the user to choose other settings to be able to update their booking.
If a user clicks inside a certain booking on the Cancel booking button, that booking will be cancelled and a message comes into sight confirming that that booking has successfully been cancelled.
Below are screenshots that depict the "My Bookings" form.

![My Bookings customer](/assets/readme_image/my_bookings_customer.jpg)

![My Bookings customer logout](/assets/readme_image/my_bookings_customer_logout.jpg)

![My Bookings customer update booking green edit button](/assets/readme_image/my_bookings_customer_update_booking_green_edit_button.jpg)

![My Bookings customer update alert successfully](/assets/readme_image/my_bookings_customer_update_alert_successfully.jpg)

![My Bookings customer already booked alert](/assets/readme_image/my_bookings_customer_update_booking_alert_table_already_booked.jpg)

![My Bookings customer cancel booking successfully](/assets/readme_image/my_bookings_customer_cancel_booking_successfully.jpg)


## Logout

The Logout button appears on the nav bar only after a user will have login.
When a user clicks on the "Logout" button on the nav bar, user will successfully logout and redirect to home page.

![Customer_logout](/assets/readme_image/my_bookings_customer_logout.jpg)


# Technologies Used

Frontend: HTML, CSS, JavaScript
Backend: Django, Django REST framework
Database: PostgreSQL

# Typography and color scheme

Google font have been used: "Roboto" and "sans serif".
Colors have been applied: #5a9bd4, #214d71, #008000, #957873, #ff4500, and #FFFFFF.

# Wireframes

I used Balsamiq wireframes for my project.

# Entity relationship diagram

![Diagram](/assets/readme_image/diagram.jpg)


# Technology Overview

## Visual Studio
Visual Studio is a robust development environment I employed for writing, reviewing, integrating, and deploying code.

## GitHub
GitHub is a platform for version control and collaborative software development. I utilized it to create a central code repository and manage the deployment of Restaurant No1. This tool allows me to track changes made to the code and revert to previous versions when necessary.

## Heroku
Heroku is a cloud-based platform that enables developers to build, deploy, and scale modern applications seamlessly. Supporting multiple programming languages including Node.js, Ruby, Java, PHP, Python, Go, Scala, and Clojure, Heroku allows developers to focus on code rather than infrastructure. I deployed Restaurant No1 on Heroku, taking advantage of its seamless integration with GitHub.

## Django & Python
Python is a high-level, general-purpose programming language. Django, a free and open-source Python-based web framework, follows the model-template-views (MTV) architectural pattern. I utilized Django and Python to develop the core functionalities of Restaurant No1.

## HTML (HyperText Markup Language)
HTML is the standard markup language for documents designed to be displayed in a web browser. It defines the structure and meaning of web content, making websites accessible and enhancing search engine optimization. I employed HTML to structure the content of Restaurant No1’s web pages.

## CSS (Cascading Style Sheets)
CSS is a style sheet language used for describing the presentation of a document written in HTML or XML. I used CSS to add styling to the HTML templates of Restaurant No1.

## JavaScript
JavaScript is a programming language essential for web development alongside HTML and CSS. I utilized JavaScript to enhance the functionality of customer registration, table booking, and cancellation processes for Restaurant No1.

## Google Fonts
Google Fonts enhance the visual appeal of websites. I incorporated Google fonts in Restaurant No1: "Roboto/sans-serif".

## W3C HTML & CSS Validators
The W3C provides online tools to validate HTML and CSS code by URL, file upload, or direct input. I used these validators to ensure the HTML and CSS code of Restaurant No1 adhered to web standards.

## CI Python Linter
The CI Python Linter, an online tool provided by Code Institute, was used to validate all Python files of Restaurant No1 through direct code input.

## JSHint
JSHint is an online tool for validating JavaScript code. I used JSHint to ensure the JavaScript code in Restaurant No1 was error-free and followed best practices.

## Balsamiq Wireframes
Balsamiq Wireframes is a graphical user interface wireframe builder application. It allows designers to arrange pre-built widgets using a drag-and-drop editor. I utilized Balsamiq to create wireframes for Restaurant No1.

## Lucidchart
Lucidchart is a web-based diagramming application that facilitates collaborative drawing, revising, and sharing of charts and diagrams. I used it to create the entity relationship diagram for Restaurant No1.

## Pexels
Pexels.com is a platform that provides high-quality and completely free stock photos licensed under the Pexels license. I used Pexels.com to source and manage visual content for Restaurant No1.

## ElephantSQL
ElephantSQL is a PostgreSQL database hosting service that manages administrative tasks such as installation, upgrades, and backups. I utilized ElephantSQL to host the PostgreSQL database for Restaurant No1.

## Gunicorn
Gunicorn is a WSGI server that acts as an intermediary between web servers and Python applications. I installed Gunicorn in Restaurant No1 to deploy the Django application on Heroku.

# Code validation

## HTML
I validated it by means of the W3C HTML validator.
Below is a screenshot that documents this validation; errors were shown.

![W3C HTML Home Page validator 1/2](/assets/readme_image/home_html_validator1.jpg)

![W3C HTML Home Page validator 2/2](/assets/readme_image/home_html_validator2.jpg)

![W3C HTML Admin validator](/assets/readme_image/admin_html_validator1.jpg)

![W3C HTML Customer validator](/assets/readme_image/customer_html_validator.jpg)

![W3C HTML Admin Dashboard validator 1/2](/assets/readme_image/admin_dashboard_html_validator1.jpg)

![W3C HTML Admin Dashboard validator 2/2](/assets/readme_image/admin_dashboard_html_validator2.jpg)

![W3C HTML Registar Customer validator](/assets/readme_image/registar_customer_html_validator.jpg)

![W3C HTML Customer Dashboard validator](/assets/readme_image/customer_dashboard_html_validator.jpg)

## CSS
I validated it by means of the W3C CSS validator.
Below is a screenshot that documents this validation; errors were shown.

![W3C CSS Home Page validator](/assets/readme_image/homepage_css_validator.jpg)

![W3C CSS Admin validator](/assets/readme_image/admin_css_validator.jpg)

![W3C CSS Admin Dashboard validator](/assets/readme_image/admin_dashboard_css_validator.jpg)

![W3C CSS Customer validator](/assets/readme_image/customer_css_validator.jpg)

![W3C CSS Customer Dashboard validator](/assets/readme_image/customer_dashboard_css_validator.jpg)

![W3C CSS Register Customer validator](/assets/readme_image/register_customer_css_validator.jpg)

## CI Python Linter
I validated it by means of CI Python Linter.
Below is a screenshot that documents this validation; errors were shown.

![CI Python Linter admin.py ](/assets/readme_image/admin.py.jpg)

![CI Python Linter apps.py](/assets/readme_image/apps.py.jpg)

![CI Python Linter tests.py](/assets/readme_image/tests.py.jpg)

![CI Python Linter views.py](/assets/readme_image/views.py.jpg)

![CI Python Linter manage.py](/assets/readme_image/manage.py.jpg)

![CI Python Linter models.py](/assets/readme_image/models.py.jpg)


# Test Cases

## User Registration and Login

### Test Case: User Registration

Description: Verify that a new user can register successfully.
Steps: Navigate to the registration page.
Fill in the required fields (username, email, password, etc.).
Submit the registration form.
Verify that a confirmation message is displayed.
Verify that the user is redirected to the login page.
Expected Result: User is registered successfully and redirected to the login page.

### Test Case: User Login

Description: Verify that a registered user can log in successfully.
Steps: Navigate to the login page.
Enter valid credentials (username and password).
Submit the login form.
Verify that the user is redirected to my bookings form.
Expected Result: User is logged in successfully and redirected to the my bookings form.

## Table Booking

### Test Case: Table Booking

Description: Verify that a user can book a table successfully.
Steps: Log in to the website.
Navigate to the table booking form.
Select a date, time, and number of guests.
Submit the booking form.
Verify that a confirmation message is displayed.
Verify that the booking details are displayed in the user's account.
Expected Result: Table is booked successfully and booking details are displayed in the user's account.

### Test Case: Table Booking Cancellation

Description: Verify that a user can cancel a table booking.
Steps: Log in to the website.
Navigate to the user's account page.
Locate the table booking to be cancelled.
Click the cancel button next to the booking.
Confirm the cancellation.
Verify that the booking is removed from the user's account.
Expected Result: Table booking is cancelled and removed from the user's account.

## Menu and Orders

### Test Case: View Menu

Description: Verify that users can view the restaurant menu.
Steps: Navigate to the menu page.
Verify that the menu items are displayed with details (name, description, price).
Expected Result: Menu items are displayed correctly with all details.

## Contact and Feedback

### Test Case: Submit Contact Form

Description: Verify that a user can submit a contact form successfully.
Steps: Navigate to the contact page.
Fill in the required fields (name, email, message).
Submit the contact form.
Expected Result: Contact form is submitted successfully.

## General Functionality

### Test Case: Responsive Design

Description: Verify that the website is responsive and displays correctly on various devices.
Steps: Open the website on different devices (desktop, tablet, mobile).
Verify that the layout adjusts correctly to the screen size.
Verify that all functionalities work as expected on each device.
Expected Result: Website displays correctly and functions as expected on all devices.

### Test Case: Navigation Links

Description: Verify that all navigation links work correctly.
Steps: Click on each navigation link in the menu.
Verify that the user is redirected to the correct page.
Verify that the content of the page matches the link description.
Expected Result: Navigation links work correctly and redirect to the appropriate pages.


# Deployment Instructions for Restaurant No1

## Via Visual 

Studio Create a GitHub Repository: Set up a new repository on GitHub for your project.
Set Up Visual Studio Workspace: Open Visual Studio, and clone your GitHub repository to create a local workspace.
Build and Deploy: Use the terminal in Visual Studio to run the necessary commands to build and deploy your website.
Save Your Work: Save your work in the Visual Studio workspace, and use Git commands to add, commit, and push changes to GitHub.
Install Dependencies: Ensure all required modules are listed in the requirements.txt file for smooth deployment.

## Via GitHub

Create a GitHub Account and Repository: Open GitHub, sign in, and create a new repository.
Link Visual Studio Workspace: Use the repository link to set up a workspace in Visual Studio.
Develop and Save: Develop your project in Visual Studio, and use Git commands to save and push your code to GitHub.

## Via Heroku 

Set Up Heroku Account: Sign up for Heroku, selecting appropriate options such as role (e.g., student) and development language (Python).
Create Heroku App: Create a new app on Heroku, configuring necessary settings like app name and region.
Configure Settings and Deploy: Set up config variables and deploy methods. Link to your GitHub repository, and deploy your app either manually or automatically. 
Run and Test: After deployment, start or restart your app to ensure it is running correctly.
Preparing Your Environment
Create a Django Project and App: Set up your Django project and create necessary apps.
Migrate and Test: Run migrations and test the server to ensure everything is set up correctly.
Set Up External Database: Create a new database on ElephantSQL and link it to your project.
Manage Static and Media Files: Use Cloudinary to store static and media files, and configure the settings accordingly.
Finalize and Deploy: Make necessary adjustments in settings, create a Procfile, and deploy your project to Heroku.


# Credits
Django Project: Utilized the Django framework to build the core of the Restaurant No1 website.
W3Schools Django Tutorial: Followed the comprehensive Django tutorial provided by W3Schools for foundational guidance and best practices.
Python.org: Referenced official Python documentation and resources available at Python.org for language-specific details and advanced features.


# Getting Started

Prerequisites
Python 3.6+
PostgreSQL
Virtual environment tool (e.g., venv)
Heroku CLI (for deployment)


# Installation

1. Repository:
   https://github.com/ROCK3879/restaurant_booking_1.git
   
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
   Open your web browser and go to https://restaurant-booking-no1-ae7b2991e60d.herokuapp.com/

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


Requirements.txt

asgiref==3.8.1
dj-database-url==2.2.0
Django==5.0.7
django-cors-headers==4.4.0
django-heroku==0.3.1
djangorestframework==3.15.2
gunicorn==22.0.0
mysqlclient==2.2.4
packaging==24.1
psycopg2==2.9.9
py==1.11.0
sqlparse==0.5.1
typing_extensions==4.12.2
tzdata==2024.1
whitenoise==6.7.0
