# MYSQL CRUD Application

A custom Django-based CRUD project for managing users, products, categories, and brands with role-based access control. It includes a landing page, custom authentication, product inventory management, and a dashboard-style admin interface.

## Overview

This project is built with Django and uses MySQL as the database backend. It includes:

- User registration and login
- Custom user model with roles (`admin`, `manager`, `user`)
- Dashboard and profile pages
- Product CRUD operations
- Category and brand management
- Soft delete and recovery for categories and brands
- Admin panel for role management and user deletion
- Image upload support for products

## Tech Stack

- Python 3.x
- Django 5.2
- MySQL
- Pillow
- HTML, CSS, JavaScript
- Django Template Engine

## Project Structure

```text
Custom Crud/
├── core/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── Products/
│   ├── admin.py
│   ├── apps.py
│   ├── decorators.py
│   ├── migrations/
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── UserAuth/
│   ├── admin.py
│   ├── apps.py
│   ├── backends.py
│   ├── migrations/
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── Users/
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── migrations/
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── static/
│   └── css/
├── templates/
│   ├── Auth/
│   ├── ProductTemplate/
│   ├── Base.html
│   └── LandingPage.html
├── media/
├── manage.py
├── notes.md
├── requirements.txt
├── venv/
└── README.md
```

## Core Features

### Authentication and user management

The project uses a custom authentication backend that allows login using either username or email.

Features include:

- User registration
- Login and logout
- Profile view
- Admin-only user management
- Role updates (`admin`, `manager`, `user`)
- Deleting user accounts from admin dashboard

### Product management

Products are managed using Django models and templates.

Supported actions:

- Add product
- View all products
- Filter products by category and brand
- Update product details
- Delete product
- Upload product image

### Category and brand management

The application supports:

- Creating new categories and brands
- Listing category and brand records
- Soft delete for brand records
- Active/deactive status for categories
- Recovery of deleted items

### Role-based access

The app restricts features based on the logged-in user's role:

- `admin`: full access, can manage users, modify products, and manage categories/brands
- `manager`: can manage product inventory and related content
- `user`: can access general pages and product listings but cannot manage products

## Database and Models

### Custom user model

The custom user model is defined in `UserAuth/models.py` and includes:

- `first_name`
- `last_name`
- `username`
- `email`
- `phone_number`
- `country_name`
- `address`
- `city`
- `role`
- `is_active`
- `is_admin`

### Product model

The product table includes:

- `p_name`
- `p_price`
- `p_image`
- `category` (ForeignKey)
- `brand` (ForeignKey)

### Category model

- `name`
- `status` (`Active` / `Deactive`)

### Brand model

- `name`
- `is_delete` (soft deletion flag)

## Application Routes

### Authentication routes

- `/` → landing page
- `/login/` → login page
- `/register/` → registration page
- `/logout/` → logout
- `/dashboard/` → dashboard
- `/profile/` → user profile
- `/manageusers/` → admin user management
- `/change-role/<user_id>/` → change user role
- `/delete-user/<user_id>/` → delete user

### Product routes

- `/products/` → list products
- `/addproduct/` → add new product
- `/updateproduct/<id>/` → update a product
- `/deleteproduct/<id>/` → delete a product
- `/category/` → category management
- `/brand/` → brand management
- `/deletecategory/<id>/` → deactivate category
- `/recovercategory/<id>/` → reactivate category
- `/deletebrand/<id>/` → soft delete brand
- `/recoverbrand/<id>/` → recover deleted brand

## Configuration Details

The project configuration is set in `core/settings.py`.

Important settings include:

- Project name: `core`
- Debug mode: enabled (`DEBUG = True`)
- MySQL database connection configured as:
  - Database name: `crud_db`
  - User: `root`
  - Password: `12345678`
  - Host: `127.0.0.1`
  - Port: `3306`
- Static files directory: `static/`
- Media directory: `media/`
- Custom auth user model: `UserAuth.CustomUser`
- Authentication backend: custom email-or-username backend

## Prerequisites

Before running the project, make sure you have:

- Python installed
- MySQL server installed and running
- A database named `crud_db` created in MySQL
- Django environment configured
- `venv` available (already included in the project folder)

## Setup Instructions

### 1. Open project folder

```bash
cd "C:\Users\Talha\OneDrive\Documents\Custom Crud"
```

### 2. Activate the virtual environment

On Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

### 3. Install dependencies

If the environment is already configured, skip this step. Otherwise install the required packages:

```bash
pip install django mysqlclient pillow argon2-cffi
```

### 4. Create database

In MySQL, create the database:

```sql
CREATE DATABASE crud_db;
```

### 5. Run database migrations

```bash
python manage.py migrate
```

### 6. Create a superuser

```bash
python manage.py createsuperuser
```

### 7. Run the development server

```bash
python manage.py runserver
```

Then open:

```text
http://127.0.0.1:8000/
```

## Default User Roles

This application is designed around these roles:

- `admin` – full administrative access
- `manager` – product and catalog management access
- `user` – general browsing and normal access

## Templates and UI

The project includes custom templates under `templates/`, such as:

- `LandingPage.html`
- `Base.html`
- `Auth/Login.html`
- `Auth/RegisterUser.html`
- `Auth/Profile.html`
- `Auth/manage_users.html`
- `ProductTemplate/Products.html`
- `ProductTemplate/AddProduct.html`
- `ProductTemplate/UpdateProduct.html`
- `ProductTemplate/Category.html`
- `ProductTemplate/Brand.html`

These templates use custom CSS and JavaScript files from the `static/` folder to create the dashboard-style UI.

## Notes

- This project appears to be a custom learning/portfolio CRUD app rather than a production-ready SaaS platform.
- `DEBUG` is set to `True`, which is intended only for local development.
- `ALLOWED_HOSTS` is currently left empty, which is acceptable for development but not recommended for deployment.
- The project uses a custom user model and custom authentication backend to support login by username or email.
- The `Users` app contains commented legacy code and is not the primary active app in the current implementation.

## Future Enhancements

Possible improvements for this project include:

- Replacing hardcoded database credentials with environment variables
- Adding validation and form classes for cleaner input handling
- Improving password reset flow
- Adding product categories and brands as separate admin modules with richer analytics
- Creating full test coverage
- Preparing the application for deployment on production hosting

## License

This project does not include a formal open-source license file. Use it for educational or local development purposes unless otherwise specified by the original author.

## Contribution

This project is a custom CRUD application and can be extended by adding:

- new report pages
- search and sorting features
- API endpoints
- better security policies
- deployment configuration

## Contact / Project Ownership

This project appears to be a local custom implementation created for Django CRUD exercises and learning purposes. Any further details should be confirmed with the project owner or repository maintainer.
