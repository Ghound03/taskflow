# TaskFlow

TaskFlow is a full-stack Django web application for managing personal tasks. Users can register, log in, create tasks, update progress, filter tasks, and view dashboard statistics.

## Project Overview

This project was created for the Full Stack Web Application Development final assignment. The aim of the project is to demonstrate front-end development, back-end development, authentication, database management, API integration, automated testing, version control, and deployment.

## Features

- User registration
- User login and logout
- Protected dashboard
- Create, read, update, and delete tasks
- Task priority levels
- Task status tracking
- Due dates
- Search functionality
- Filter by status
- Filter by priority
- Dashboard statistics
- External quote API integration
- Responsive design
- Automated tests
- Deployment-ready configuration

## Technologies Used

- Python
- Django
- SQLite for local development
- PostgreSQL for deployment
- HTML
- CSS
- JavaScript
- WhiteNoise
- Gunicorn
- Render

## User Roles

### Guest
- Can view the home page
- Can register
- Can log in

### Authenticated User
- Can access dashboard
- Can create tasks
- Can edit own tasks
- Can delete own tasks
- Can search and filter own tasks

### Admin
- Can access Django admin panel
- Can manage users and tasks

## Installation

Clone the repository:

```bash
git clone YOUR_REPOSITORY_URL
cd taskflow

## Live Website

https://taskflow-71xa.onrender.com