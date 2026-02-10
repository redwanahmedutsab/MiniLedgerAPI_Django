# Mini Ledger API

This is a simple backend REST API built with **Django** and **Django REST Framework**.  
The API allows a user to manage customers and keep track of their **credit and debit ledger entries**.

This project was created as a take-home assignment to demonstrate:
- Django REST API development
- Authentication
- Database modeling
- Basic business logic

---

## What this project does

- Users can register and log in
- Each user can manage **only their own data**
- Users can:
  - Create customers
  - Add credit/debit ledger entries for each customer
  - View customer balance summary

**Credit** → customer owes money  
**Debit** → payment received  

Balance is calculated as:

balance = total_credit − total_debit

---

## Tech Stack

- Python
- Django
- Django REST Framework
- SQLite (default database)

---

## How to run the project locally

### 1. Clone the repository
```bash
git clone <your-github-repo-link>
cd MiniLedgerAPI_Django


⸻

2. Create and activate virtual environment

python -m venv venv
source venv/bin/activate   # macOS / Linux
venv\Scripts\activate      # Windows


⸻

3. Install dependencies

pip install -r requirements.txt


⸻

4. Run migrations

python manage.py makemigrations
python manage.py migrate


⸻

5. (Optional) Create admin user

python manage.py createsuperuser


⸻

6. Start the server

python manage.py runserver

The server will run at:

http://127.0.0.1:8000/


⸻

Authentication

This API uses Token Authentication.

After registering or logging in, include the token in request headers:

Authorization: Token <your_token_here>


⸻

API Endpoints Overview

Authentication
	•	POST /api/auth/register/ – Register a new user
	•	POST /api/auth/login/ – Login and get token

⸻

Customers
	•	POST /api/customers/ – Create customer
	•	GET /api/customers/ – List customers
	•	PUT /api/customers/{id}/ – Update customer
	•	DELETE /api/customers/{id}/ – Delete customer

⸻

Ledger Entries
	•	POST /api/customers/{customer_id}/entries/ – Add credit/debit entry
	•	GET /api/customers/{customer_id}/entries/ – List entries

Filters:
	•	?type=credit
	•	?type=debit
	•	?start_date=YYYY-MM-DD&end_date=YYYY-MM-DD

⸻

Customer Summary
	•	GET /api/customers/{customer_id}/summary/

Returns:

{
  "total_credit": 5000,
  "total_debit": 2000,
  "balance": 3000
}


⸻

Postman Collection

A Postman collection is included in the repository to test all APIs easily.

File:

Mini Ledger API.postman_collection.json

Steps:
	1.	Import the collection into Postman
	2.	Login using the Auth → Login request
	3.	Token is saved automatically
	4.	Test Customers, Ledger, and Summary APIs

⸻

Notes
	•	Each user can access only their own customers and ledger entries
	•	SQLite is used for simplicity
	•	This project is intended for learning and evaluation purposes

⸻

Author

Redwan Ahmed Utsab
