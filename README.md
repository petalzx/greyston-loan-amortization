# Loan Amortization API

A FastAPI-based REST API for managing users, loans, and shared loans with amortization functionality.

---

## Features

- Create and manage users
- Create loans with amounts, interest rates, and terms
- Fetch loan schedules and summaries
- Share loans with between users

---

## Installation

1. **Clone Repository**
   ```bash
   git clone https://git@github.com:your-username/loan-amortization-api.git
   cd loan-amortization-api
2. **Set Up Virtual Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
 
---

## Running the Application
Start the API using Uvicorn
   ```bash
   # Run directly with Uvicorn (Recommended for FastAPI)
   uvicorn app.main:app --reload
   
   # Or run main function
   python -m app.main
   ```

Access the API at:
   - **Interactive Docs** : http://127.0.0.1:8000/docs
   - **Root Endpoint** : http://127.0.0.1:8000/

---

## API Endpoints
### Users
- `POST /api/endpoints/users/` - Create a user.
- `GET /api/endpoints/users/{email}` - Get a user by email.

### Loans
- `POST /api/endpoints/loans/?user_id=1` - Create a loan.
- `GET /api/endpoints/loans/{loan_id}/schedule` - Fetch loan schedule.
- `GET /api/endpoints/loans/{loan_id}/summary?month=6` - Fetch loan summary.

### Shared Loans
- `POST /api/endpoints/shared-loans/` - Share a loan.
   
