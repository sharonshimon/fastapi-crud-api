# FastAPI CRUD Application

A simple FastAPI web server that provides RESTful CRUD endpoints for two entities:

* **User**: Fields:

  * `id` (int) — Unique identifier
  * `status` (str) — "active" or "inactive"
* **Partner**: Flexible JSON structure for storing arbitrary data

---

## 🚀 Features

* **CRUD Operations** for `User` and `Partner`
* **Data Validation** with Pydantic models
* **SQLite Database** for persistence (file: `data.db`)
* **Auto-Generated Docs** via Swagger UI and ReDoc
* **Hot Reload** during development
* **Comprehensive Tests** using pytest

---

## 🛠️ Requirements

* Python 3.9+
* `pip` package manager

---

## ⚙️ Local Setup

1. **Clone the repository**

   ```bash
   git clone https://github.com/sharonshimon/fastapi-crud-api-new.git
   cd fastapi-crud-api-new
   ```

2. **Create & activate a virtual environment**

   ```bash
   python -m venv .venv
   # Windows (PowerShell)
   .\.venv\Scripts\Activate
   # macOS/Linux
   source .venv/bin/activate
   ```

3. **Install dependencies**

   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt uvicorn[standard]
   ```

---

## ▶️ Running the Server

Start the app with hot reload:

```bash
uvicorn app.main:app --reload
```

* **Swagger UI**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
* **ReDoc**:   [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

Base API route: **`/api/v1`**

---

## 📚 API Endpoints

* **Users**

  * `GET    /api/v1/users/`
  * `POST   /api/v1/users/`
  * `GET    /api/v1/users/{id}`
  * `PUT    /api/v1/users/{id}`
  * `DELETE /api/v1/users/{id}`

* **Partners**

  * `GET    /api/v1/partners/`
  * `POST   /api/v1/partners/`
  * `GET    /api/v1/partners/{id}`
  * `PUT    /api/v1/partners/{id}`
  * `DELETE /api/v1/partners/{id}`

---

## 🧪 Testing

Run the test suite:

```bash
pytest
```

Tests use an in-memory SQLite database to ensure a clean state each run.

---

## 🗂️ Project Structure

```
fastapi-crud-api-new/       # repo root
├── app/                    # application package
│   ├── crud/               # core CRUD logic
│   ├── db.py               # DB setup & session
│   ├── main.py             # FastAPI app entrypoint
│   ├── models.py           # SQLAlchemy & Pydantic schemas
│   └── routers/            # API route definitions
├── tests/                  # unit & integration tests
├── requirements.txt        # pinned dependencies
└── README.md               # this file
```

---

## 🚫 Excluding the Virtual Environment

Add to `.gitignore`:

```gitignore
.venv/
venv/
```

Remove any tracked venv folder:

```bash
git rm -r --cached .ve
```
