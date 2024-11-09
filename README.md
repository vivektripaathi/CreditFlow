# CreditFlow: An Credit Approval System

This project is a credit approval system built with Django and Django REST Framework, designed to assess customers' loan eligibility based on their credit history and financial profile. It supports key functionalities like registering customers, checking loan eligibility, creating loans, and viewing loan details.

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
    CREATE DATABASE credit_flow_db_docker1;
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
