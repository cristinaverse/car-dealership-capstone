# Car Dealership Capstone Project

A full-stack car dealership application with Django backend, React frontend, and Express-MongoDB microservices.

## Features
- Django backend with admin interface
- React frontend for user management  
- Express-MongoDB microservices for dealer data
- User authentication and authorization
- Car makes and models management
- Dealer reviews and ratings with sentiment analysis
- CI/CD pipeline with GitHub Actions
- Docker containerization

## Quick Start

### Using Docker (Recommended)
bash
`docker-compose up --build`


# Manual Setup

## Backend
cd backend
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver

## Frontend (new terminal)
cd frontend
npm install
npm start

## Microservices (new terminal)
cd microservices/express-mongo
npm install
npm start

_

# URLs

Django Backend: http://localhost:8000
React Frontend: http://localhost:3000
Express API: http://localhost:3030
Django Admin: http://localhost:8000/admin
