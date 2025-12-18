## FastAPI API with Validation

This project is a small **FastAPI** application that demonstrates basic CRUD-style endpoints with **request body validation** using **Pydantic** models.  
It uses in-memory storage for users and focuses on clean, validated input rather than persistence.

### Features

- **FastAPI-based API** with automatic interactive docs.
- **Pydantic validation** on request bodies (`UserCreate`, `UserUpdate`).
- **In-memory users collection** for simplicity (no database).
- **CRUD-style endpoints** for managing users by email.

### Tech Stack

- **Language**: Python 3.11+ (recommended)
- **Framework**: FastAPI
- **Validation**: Pydantic v2
- **ASGI server**: Uvicorn

---

## Project Structure

```text
app/
  __init__.py
  main.py      # FastAPI app instance and app configuration
  routes.py    # All API routes/endpoints
  schema.py    # Pydantic models for validation
venv/          # (Optional) Python virtual environment
```

---

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/Anticoder03/python-fast-api-validation.git
cd python-fast-api-validation
```

### 2. Create & activate a virtual environment (optional but recommended)

If you don’t already have `venv` set up, you can create one:

```bash
python -m venv venv
```

Activate it:

- **Windows (PowerShell)**:

```bash
.\venv\Scripts\Activate.ps1
```

- **Windows (CMD)**:

```bash
venv\Scripts\activate.bat
```

- **Linux / macOS**:

```bash
source venv/bin/activate
```

### 3. Install dependencies





>
> ```bash
> pip install -r requirements.txt
> ```

---

## Running the Server

From the project root (`api-with-validation`), run:

```bash
uvicorn app.main:app --reload
```

- The API will be available at: `http://127.0.0.1:8000`
- Interactive documentation:
  - Swagger UI: `http://127.0.0.1:8000/docs`
  - ReDoc: `http://127.0.0.1:8000/redoc`

---

## API Overview

All endpoints are defined in `app/routes.py` and use Pydantic schemas from `app/schema.py`.

### Health / Root

- **GET** `/`
  - **Description**: Simple health check for the API.
  - **Response example**:

    ```json
    {
      "message": "Server is running.",
      "status": "success",
      "route": "go to /users"
    }
    ```

### Create User

- **POST** `/users`
- **Body schema**: `UserCreate`

```json
{
  "name": "John Doe",
  "email": "john@example.com",
  "age": 25
}
```

**Validation rules (`UserCreate`):**

- **name**: string, required, min length = 2, max length = 50
- **email**: valid email address (`EmailStr`)
- **age**: integer, required, between 18 and 60 (inclusive)

**Sample success response:**

```json
{
  "message": "User created successfully",
  "user": {
    "name": "John Doe",
    "email": "john@example.com",
    "age": 25
  }
}
```

### Get All Users

- **GET** `/users`
- **Description**: Returns all users currently stored in memory.

**Sample response:**

```json
{
  "message": "Server is running.",
  "status": "success",
  "users": [
    {
      "name": "John Doe",
      "email": "john@example.com",
      "age": 25
    }
  ]
}
```

> Note: Users are stored only in memory (`users` list in `routes.py`).  
> Data will be lost when the server restarts.

### Update User

- **PUT** `/users/{email}`
- **Path parameter**:
  - **email**: email of the user to update (string)
- **Body schema**: `UserUpdate`

```json
{
  "name": "John Smith",
  "age": 30
}
```

**Validation rules (`UserUpdate`):**

- **name**: optional string, min length = 2 (if provided)
- **age**: optional integer, must be ≥ 18 (if provided)

If a user with the given email is found, their fields are updated (only provided fields).  
If not found, API returns:

```json
{
  "detail": "User not found"
}
```

with HTTP status **404**.

### Delete User

- **DELETE** `/users/{email}`
- **Path parameter**:
  - **email**: email of the user to delete

If a user with the given email exists, it is removed from the `users` list:

```json
{
  "message": "User deleted"
}
```

Otherwise, the API returns:

```json
{
  "detail": "User not found"
}
```

with HTTP status **404**.

---

## Notes & Limitations

- **No database**: This is designed as a **learning / demo project**; users are stored in a simple Python list.
- **Non-persistent data**: Restarting the server clears all users.
- **Identifiers**: Users are identified and updated/deleted by **email**.

---

## Extending the Project

Some ideas to build on this project:

- **Add a database** (e.g. SQLite, PostgreSQL) via SQLAlchemy or another ORM.
- **Add authentication** (JWT, OAuth2).
- **Add pagination** and filtering for `/users`.
- **Add tests** using `pytest` and `httpx` or `fastapi.testclient`.


