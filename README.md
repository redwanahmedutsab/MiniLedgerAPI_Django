# Mini Ledger API

This is a simple backend REST API built with **Django** and **Django REST Framework**.

The API allows users to manage customers and keep track of their **credit and debit ledger entries**.

This project was created as a take-home assignment to demonstrate:

* Django REST API development
* Authentication & security
* Database modeling
* Basic business logic implementation

---

## 🚀 Features

* **User Management:** Users can register and log in
* **Data Ownership:** Each user can manage **only their own data**
* **Core Functionality:**
* Create and manage customers
* Add ledger entries (credit/debit) for each customer
* View real-time customer balance summaries



---

## 💰 Financial Logic

* **Credit:** Customer owes money
* **Debit:** Payment received from customer

**Balance calculation:**
`balance = total_credit - total_debit`

---

## 🛠 Tech Stack

* **Language:** Python
* **Framework:** Django & Django REST Framework (DRF)
* **Database:** SQLite (default)

---

## 📂 Project Structure

```text
MiniLedgerAPI_Django/
│
├── MiniLedgerAPI_Django/        # Project configuration
│   ├── settings.py             # Django & DRF settings
│   ├── urls.py                 # Main URL routing
│   ├── wsgi.py
│   └── asgi.py
│
├── accounts/                   # Authentication (register & login)
│   ├── serializers.py
│   ├── views.py
│   └── urls.py
│
├── customers/                  # Customer management
│   ├── models.py
│   ├── serializers.py
│   └── views.py
│
├── ledger/                     # Ledger entries & summary
│   ├── models.py
│   ├── serializers.py
│   └── views.py
│
├── manage.py                   # Django CLI tool
├── requirements.txt            # Project dependencies
├── README.md
├── Mini Ledger API.postman_collection.json
└── db.sqlite3                  # Local database

```

---

## ⚙️ How to Run Locally

1. **Clone the repository**
```bash
git clone https://github.com/redwanahmedutsab/MiniLedgerAPI_Django
cd MiniLedgerAPI_Django

```


2. **Create and activate virtual environment**
```bash
python -m venv venv
# macOS / Linux
source venv/bin/activate
# Windows
venv\Scripts\activate

```


3. **Install dependencies**
```bash
pip install -r requirements.txt

```


4. **Run migrations**
```bash
python manage.py makemigrations
python manage.py migrate

```


5. **Start the server**
```bash
python manage.py runserver

```


The server will run at: `http://127.0.0.1:8000/`

---

## 🔑 Authentication

This API uses **Token Authentication**.

After registering or logging in, include the token in request headers:
`Authorization: Token <your_token_here>`

---

## 📡 API Endpoints Overview

### Authentication

| Method | Endpoint | Description |
| --- | --- | --- |
| POST | `/api/auth/register/` | Register a new user |
| POST | `/api/auth/login/` | Login and obtain token |

### Customers

| Method | Endpoint | Description |
| --- | --- | --- |
| GET | `/api/customers/` | List all customers |
| POST | `/api/customers/` | Create a new customer |
| PUT | `/api/customers/{id}/` | Update customer |
| DELETE | `/api/customers/{id}/` | Delete customer |

### Ledger Entries

**List / Add entries:**
`GET / POST /api/customers/{customer_id}/entries/`

**Filters:**

* `?type=credit`
* `?type=debit`
* `?start_date=YYYY-MM-DD&end_date=YYYY-MM-DD`

### Customer Summary

`GET /api/customers/{customer_id}/summary/`

**Response example:**

```json
{
  "total_credit": 5000,
  "total_debit": 2000,
  "balance": 3000
}

```

---

## 🧪 Postman Collection

A Postman collection is included in the root directory to test all endpoints.

* **File:** `Mini Ledger API.postman_collection.json`
* **Usage:** Import into Postman, use the Login endpoint, and the token will be applied automatically to subsequent requests.

---

## ✍️ Author

**Redwan Ahmed Utsab**
