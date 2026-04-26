# iPhone Sales API

A RESTful backend service built with FastAPI for managing iPhone sales data.
The API supports CRUD operations, filtered queries, and basic sales analytics, backed by PostgreSQL and SQLAlchemy.

The project is structured with clear separation of concerns (routing, business logic, persistence), making it easy to extend and maintain.

---

## Tech Stack

* FastAPI
* SQLAlchemy ORM
* PostgreSQL
* Pydantic (validation)
* Uvicorn (ASGI server)

---

## Project Setup

### 1. Clone the repository

```bash
git clone <repository-url>
cd iphone-sales-api
```

### 2. Create a virtual environment

```bash
python -m venv env
```

### 3. Activate the environment

**Windows**

```bash
env\Scripts\activate
```

**Linux / Mac**

```bash
source env/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure environment variables

Create a `.env` file in the root directory:

```env
DATABASE_URL=postgresql://<username>:<password>@<host>:5432/<database_name>
```

---

## Running the Application

Start the development server:

```bash
uvicorn main:app --reload

```
or
```bash

fastapi dev
```
The API will be available at:

```
http://127.0.0.1:8000/
```

A custom Swagger UI is served at the root endpoint.

---
### Testing Instruction by the postman endpoints and the response

--- Post API endpoint ---

<img width="1444" height="867" alt="Screenshot 2026-04-26 111215" src="https://github.com/user-attachments/assets/75182e5b-2ab7-4d39-8bdc-da67be4c8334" />

--- Get API endpoint ---
<img width="1437" height="878" alt="Screenshot 2026-04-26 111315" src="https://github.com/user-attachments/assets/ec45121a-9611-431a-a505-c85866ea94b7" />




