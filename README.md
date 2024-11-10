# CreditFlow: An Credit Approval System

This project is a credit approval system built with Django and Django REST Framework, designed to assess customers' loan eligibility based on their credit history and financial profile. It supports key functionalities like registering customers, checking loan eligibility, creating loans, and viewing loan details.

## Table of Contents

- **[Technologies](#technologies)**
- **[Project Setup](#project-setup)**
- **[API Endpoints](#api-endpoints)**
- **[Code Structure](#code-structure)**

## Technologies

- **Python 3.10+**
- **Django 4+**
- **Django REST Framework**
- **PostgreSQL**
- **Celery**
- **Redis**
- **Docker and Docker Compose**

## Project Setup

1. **Clone the Repository**:

    ```bash
    git clone https://github.com/vivektripaathi/CreditFlow
    cd CreditFlow
    ```

2. Make sure **PostgreSQL and Docker is installed and running** on your machine:

3. **Create a PostgreSQL database** named `credit_flow_db`:

    ```sql
    CREATE DATABASE credit_flow_db;
    ```

3. **Environment Variables**:

    1. **Rename the provided .env.example file to .env in the project root**:

    ```bash
    mv .env.example .env
    ```

    2. **Edit the .env File**: Open the .env file and update the variables with your values.

    ```bash
    POSTGRES_DB=__YOUR_DB_NAME__
    POSTGRES_USER=__YOUR_DB_NAME__
    POSTGRES_PASSWORD=__YOUR_DB_PASSWORD__
    ```

4. **Run Docker compose**:

    ```bash
    docker-compose up --build
    ```

## API Endpoints

- **Register Customer**: `http://127.0.0.1:8000/customer/register/`
- **View Loans**: `http://localhost:8000/loan/view_loans/14`
- **Check eligibility**: `http://localhost:8000/loan/check-eligibility/`
- **Create Loan**: `http://localhost:8000/loan/create-loan/`
- **View Loan**: `http://localhost:8000/loan/view_loan/14`

## Code Structure

This project is modularized into multiple apps, each responsible for a specific functionality. The main apps are:

- **CreditFlow**: The core application that ties together all other components.
- **core**: Contains utilities and shared logic used across the project.
- **customer**: Manages customer-related logic and models.
- **loan**: Manages loan-related logic and models.

Each app follows a consistent folder structure that separates the different layers of functionality. Here’s an overview:

```plaintext
/app_name
├── data
│   ├── __init__.py
│   ├── abstract_repo.py    # Defines repository interfaces (abstractions).
│   └── db_repo.py          # Implements data access and interaction with the database.
│
├── domain
│   ├── __init__.py
│   ├── domain_models.py    # Defines core models for the domain.
│   └── use_cases           # Contains business logic and use cases for each feature.
│       ├── __init__.py
│       ├── 1_use_case.py   # Specific use cases (e.g., RegisterCustomer, CheckEligibility).
│       └── 2_use_case.py
│
├── presentation
│   ├── __init__.py
│   ├── urls.py             # URL configurations for the app.
│   └── views.py            # API views for handling HTTP requests and responses.
│
├── apps.py                 # App configuration.
├── inject.py               # Dependency injection setup for repositories and use cases.
└── models.py               # Django ORM models.

```
