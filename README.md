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

## API Overview

### Create Sale

**POST** `/sales`

```json
{
  "customer_name": "John Doe",
  "phone_model": "iPhone 15",
  "color": "Black",
  "storage_gb": 128,
  "price": 79999,
  "store_location": "Delhi"
}

### Get All Sales

**GET** `/sales`

Optional query params:

* `phone_model`
* `color`

Example:

/sales?phone_model=iPhone 15&color=Black


### Get Sale by ID

**GET** `/sales/{sale_id}`


### Update Sale

**PUT** `/sales/{sale_id}`

Request body is same as create.

---

### Delete Sale

**DELETE** `/sales/{sale_id}`

---

### Sales Statistics

**GET** `/sales/stats`

Example response:

```json
{
  "total_sales": 25,
  "total_revenue": 1250000.00,
  "average_price": 50000.00,
  "most_popular_model": "iPhone 15"
}

## Project Structure

├── main.py        # Application entry point
├── database.py    # DB engine and session management
├── model.py       # SQLAlchemy models
├── schema.py      # Pydantic schemas & validation
├── service.py     # Business logic layer
├── router.py      # API routes


## Design Decisions

### Layered Architecture

The codebase is split into three main layers:

* **Router** → handles HTTP and request/response
* **Service** → contains business logic
* **Model/DB** → persistence layer

This keeps endpoints thin and logic reusable.

---

### Validation Strategy

Validation is applied only where it matters:

* Enforced on **create** and **update**
* Skipped for **read** and **delete**

This avoids unnecessary overhead and keeps read endpoints fast.

---

### Controlled Input (Phone Models)

Allowed phone models are explicitly whitelisted.
This prevents inconsistent or messy data (e.g., "iphone15", "IPHONE 15", etc.) and ensures normalized storage.

---

### Automatic Sale Date

`sale_date` is assigned on the server using the current date.
Clients are not responsible for providing it.

This avoids incorrect or manipulated timestamps.

### Financial Precision

Prices are handled using `Decimal` instead of float.

Reason:

* Avoid floating-point rounding errors
* Maintain accuracy in revenue calculations

### Database Efficiency

* Aggregations (SUM, AVG, COUNT) are executed at the database level
* Connection pooling is enabled for better performance under load

### Flexible Filtering

Filtering uses case-insensitive matching (`ILIKE`), allowing partial matches without strict formatting requirements.

## Notes / Assumptions

* The system assumes a controlled environment where only valid iPhone models are allowed.
* Currency is not explicitly stored (assumed consistent across records).
* No authentication/authorization is implemented (can be added depending on use case).
* Pagination is not included but can be easily integrated.

## Possible Improvements

* Add JWT-based authentication
* Pagination and sorting support
* Dockerization
* Unit and integration tests
* Rate limiting / caching layer

---

## Running in Production

For production, consider:

* Using Gunicorn with Uvicorn workers
* Managing secrets via environment configs or vaults
* Setting up proper logging and monitoring

---

## Author

Vishal Shrivastava
