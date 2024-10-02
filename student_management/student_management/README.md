# Student Management System

A Django-based application for managing student records with an enhanced user interface using Bootstrap.

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Setup Instructions](#setup-instructions)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Technologies Used](#technologies-used)
- [Acknowledgments](#acknowledgments)
- [Contact](#contact)

## Features

- **Add**, **edit**, and **view** student information.
- **User authentication** for secured access to sensitive operations.
- **Search** functionality to find students by name.
- **Pagination** to navigate through lists of students.
- **Form validation** and **error handling** to ensure data integrity.
- **Responsive UI** enhanced with **Bootstrap** for better user experience.



## Prerequisites

- **Python 3.x**
- **Git**
- **Virtual Environment (optional but recommended)**

## Setup Instructions

Follow these steps to set up and run the project locally.

### 1. Clone the repository

```bash
git clone https://github.com/your_username/student_management.git
cd student_management
```
### 2. Create a virtual environment
```bash
python -m venv venv
```
####Activate the virtual environment
* **For Windows:**
```bash
venv\Scripts\activate
```
* **For macOS/Linux:**
```bash
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```
### 4. Apply migrations
```bash
python manage.py migrate
```
### 5. Collect static files
```bash
python manage.py collectstatic
```
### 6. Create a superuser
```bash
python manage.py createsuperuser
```
### 7. Run the development server
```bash
python manage.py runserver
```
### 8. Access the application
* Open your web browser and navigate to http://127.0.0.1:8000/ to access the application.
* To access the admin panel, go to http://127.0.0.1:8000/admin/ and log in with your superuser credentials.

## Usage
* **Home Page / Student List:**
	* View a list of all students with pagination controls.
	* Use the search bar to find students by their first or last name.
	* Click on a student's name to view their details.
* **Authentication:**
	* Log in using the credentials of the superuser or any staff user.
	* Only authenticated users can add or edit student records
* **Add New Student:**
	* Click on the "Add New Student" button (visible when logged in) to open the student creation form.
	* Fill in the student's information and submit.
* **Edit Student Information:**
	 * On the student detail page, click the "Edit Student" button (visible when logged in) to modify student details.
* **Logout**
	* Click the "Logout" link in the navigation bar to end your session.
	
## Project Structure
```stylus
student_management/
├── student_management/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── students/
│   ├── __init__.py
│   ├── migrations/
│   │   └── __init__.py
│   ├── templates/
│   │   ├── students/
│   │   │   ├── student_list.html
│   │   │   ├── student_detail.html
│   │   │   └── student_form.html
│   │   └── registration/
│   │       └── login.html
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── templates/
│   ├── base.html
│   ├── 404.html
│   └── 500.html
├── static/
│   ├── css/
│   │   └── styles.css
│   └── screenshots/
│       ├── student_list.png
│       ├── student_detail.png
│       ├── add_student.png
│       └── login_page.png
├── manage.py
├── requirements.txt
└── README.md
```
## Technologies Used
* **Django:** Web framework for rapid development.
* **Bootstrap 4:** Front-end component library for responsive design.
* **SQLite:**database for development.
* **HTML/CSS:** Templating and styling.
* **Python:** Backend programming language.

## Acknowledgments
* Inspired by Django's official documentation and tutorials.
* UI enhanced using [Bootstrap](https://getbootstrap.com/)

## Contact
* **Project Maintainer:**Fangyuan Lin
* **Email:**flin025@uottawa.ca