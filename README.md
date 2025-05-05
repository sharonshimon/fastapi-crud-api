# FastAPI CRUD Application

This project is a FastAPI-based web server that implements RESTful CRUD endpoints for two entities:
- **User**: Contains fields `id` (integer) and `status` (active/inactive).
- **Partner**: Has an open-ended structure to store arbitrary JSON data.

The application uses SQLite as the database and includes comprehensive unit and integration tests.

---

## Features
- **CRUD Operations**: Create, Read, Update, and Delete endpoints for `User` and `Partner`.
- **Validation**: Input validation using Pydantic models.
- **Auto-Generated Documentation**: Swagger UI and ReDoc available at runtime.
- **Testing**: Comprehensive test suite using `pytest`.

---

## Requirements
- Python 3.9 or higher
- `pip` (Python package manager)

---

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/fastapi-crud.git
   cd fastapi-crud
   ```

2. **Create a Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

---

## Running the Application

1. **Start the Server**:
   ```bash
   uvicorn app.main:app --reload
   ```

2. **Access the API Documentation**:
   - Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
   - ReDoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

3. **API Endpoints**:
   - Base URL: `http://127.0.0.1:8000/api/v1`
   - Example Endpoints:
     - `GET /users/`: List all users.
     - `POST /users/`: Create a new user.
     - `GET /partners/`: List all partners.
     - `POST /partners/`: Create a new partner.

---

## Testing

1. **Run Tests**:
   ```bash
   pytest
   ```

2. **Test Coverage**:
   - Ensure all tests pass and the application behaves as expected.

---

## Project Structure

```
fastapi-crud/
├── app/
│   ├── crud/               # CRUD logic for User and Partner
│   ├── db.py               # Database configuration
│   ├── main.py             # FastAPI application entry point
│   ├── models.py           # SQLAlchemy and Pydantic models
│   ├── routers/            # API routers for User and Partner
├── tests/                  # Unit and integration tests
├── requirements.txt        # Project dependencies
└── README.md               # Project documentation
```

---

## Notes
- The application uses SQLite as the database, which stores data in a file named `data.db`.
- For testing, an in-memory SQLite database is used to ensure a clean state for each test.

---

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## Contact
For any questions or feedback, feel free to reach out at [your-email@example.com].
