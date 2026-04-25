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

The API will be available at:

```
http://127.0.0.1:8000/
```

A custom Swagger UI is served at the root endpoint.

---

