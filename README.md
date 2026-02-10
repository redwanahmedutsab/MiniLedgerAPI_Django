# Mini Ledger API

This is a simple backend REST API built with **Django** and **Django REST Framework**.

The API allows a user to manage customers and keep track of their **credit and debit ledger entries**.

This project was created as a take-home assignment to demonstrate:

* Django REST API development
* Authentication
* Database modeling
* Basic business logic

---

## What this project does

* Users can register and log in
* Each user can manage **only their own data**
* Users can:
* Create customers
* Add credit/debit ledger entries for each customer
* View customer balance summary



**Credit** → customer owes money

**Debit** → payment received

**Balance is calculated as:**


---

## Tech Stack

* **Language:** Python
* **Framework:** Django & Django REST Framework
* **Database:** SQLite (default)

---

## Project Structure

```text
MiniLedgerAPI_Django/
│
├── core/                       # Project configuration
│   ├── settings.py             # App settings & DRF configuration
│   ├── urls.py                 # Main routing (includes app URLs)
│   └── wsgi.py
│
├── api/                        # Main application logic
│   ├── migrations/             # Database migrations
│   ├── models.py               # Customer and LedgerEntry models
│   ├── serializers.py          # DRF Serializers for JSON conversion
│   ├── views.py                # API Logic (List, Create, Summary)
│   ├── urls.py                 # API Endpoints
│   └── admin.py                # Admin panel configurations
│
├── venv/                       # Virtual environment (ignored by git)
├── manage.py                   # Django CLI tool
├── requirements.txt            # Project dependencies
├── Mini Ledger API.json        # Postman collection for testing
└── db.sqlite3                  # Local database (generated after migration)

```

---

## How to run the project locally

### 1. Clone the repository

```bash
git clone <your-github-repo-link>
cd MiniLedgerAPI_Django

```

### 2. Create and activate virtual environment

```bash
python -m venv venv
source venv/bin/activate   # macOS / Linux
venv\Scripts\activate      # Windows

```

### 3. Install dependencies

```bash
pip install -r requirements.txt

```

### 4. Run migrations

```bash
python manage.py makemigrations
python manage.py migrate

```

### 5. (Optional) Create admin user

```bash
python manage.py createsuperuser

```

### 6. Start the server

```bash
python manage.py runserver

```

The server will run at: `http://127.0.0.1:8000/`

---

## Authentication

This API uses **Token Authentication**. After registering or logging in, include the token in your request headers:

`Authorization: Token <your_token_here>`

---

## API Endpoints Overview

### Authentication

* `POST /api/auth/register/` – Register a new user
* `POST /api/auth/login/` – Login and get token

### Customers

* `GET /api/customers/` – List all customers
* `POST /api/customers/` – Create a new customer
* `PUT /api/customers/{id}/` – Update customer details
* `DELETE /api/customers/{id}/` – Delete a customer

### Ledger Entries

* `GET /api/customers/{customer_id}/entries/` – List all entries for a customer
* `POST /api/customers/{customer_id}/entries/` – Add a credit/debit entry

**Filters:**

* `?type=credit`
* `?type=debit`
* `?start_date=YYYY-MM-DD&end_date=YYYY-MM-DD`

### Customer Summary

* `GET /api/customers/{customer_id}/summary/`

**Response Example:**

```json
{
  "total_credit": 5000,
  "total_debit": 2000,
  "balance": 3000
}

```

---

## Postman Collection

A Postman collection is included in the repository to test all APIs easily.

**File:** `Mini Ledger API.postman_collection.json`

1. Import the collection into Postman.
2. Login using **Auth → Login**.
3. Token is usually saved to a variable or must be copied to headers.
4. Test Customers, Ledger, and Summary APIs.

---

## Notes

* **Privacy:** Each user can access only their own customers and ledger entries.
* **Database:** SQLite is used for simplicity and ease of setup.
* **Purpose:** This project is intended for learning and evaluation purposes.

---

## Author

**Redwan Ahmed Utsab**