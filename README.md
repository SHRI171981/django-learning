# Django CRM

## Problem statement

Small businesses need a way to keep track of customers, products and orders, with different access for staff and customers. Learning Django well means building something with real models, authentication and permissions, not just following isolated examples.

## Solution

A customer relationship management web app built with Django. Admins manage customers, products and orders from a dashboard. Customers register, log in and see only their own orders, and can update their account settings and profile picture.

## Tech stack

Python, Django, SQLite, django-filter, HTML templates with Bootstrap.

## Features

- **Models** for customers, products (with categories and many-to-many tags) and orders, linked by one-to-one, foreign-key and many-to-many relationships
- **Authentication** with registration, login and logout
- **Role-based access** through custom decorators: admin-only dashboard, customer-only user page, and redirects for signed-in or signed-out users
- **Admin dashboard** showing customers and orders with their status
- **Order management** to create, update and delete orders for a customer
- **Search and filtering** of orders by date range and note text
- **Account settings** with a profile picture upload
- Commented models explaining the Django concepts used

## Future steps

- REST API on top of the models
- Automated tests for views and permissions
- Order totals, invoices and status reports
- Deployment with PostgreSQL

## Getting started

```bash
cd crm
pip install django django-filter pillow
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```
