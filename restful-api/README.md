# RESTful API Exercises

> Build small HTTP services with `requests`, `http.server`, and Flask.

## Description & Objectives

This project incrementally explores REST-style endpoints, first with remote API consumption, then with a custom HTTP server, and finally with a Flask application that adds authentication and security concepts.

## Technologies Used

| Tool | Purpose |
| --- | --- |
| Python 3 | Language used for all exercises |
| `requests` | HTTP client for consuming JSONPlaceholder |
| `http.server` | Standard-library HTTP server example |
| Flask | Web framework for API routes |
| `flask_httpauth` | Basic Auth support |
| `flask_jwt_extended` | JWT authentication and authorization |

## Prerequisites

- Python 3.10 or newer
- `pip` and virtual environment support
- Internet access for the `requests` task that calls JSONPlaceholder
- Packages: `flask`, `requests`, `flask_httpauth`, `flask_jwt_extended`

## Installation

Create and activate a virtual environment, then install the dependencies:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install flask requests flask_httpauth flask_jwt_extended
```

## Usage

Example Flask run:

```bash
python3 task_04_flask.py
```

Example request:

```bash
curl http://127.0.0.1:5000/
curl -X POST http://127.0.0.1:5000/add_user -H 'Content-Type: application/json' -d '{"username":"alice"}'
```

Other tasks can be run directly as scripts or imported from Python for testing.

## Features

- Fetch and display remote JSON data
- Export API results to CSV
- Build a minimal HTTP server with multiple routes
- Create a Flask API with validation and error handling
- Add Basic Auth and JWT-protected routes

## Screenshots

No screenshots are included because the project is terminal-driven. Example API responses can be captured with `curl` or your browser.

## Documentation Standard

The Python modules follow [PEP 257](https://peps.python.org/pep-0257/) docstrings for modules, functions, and classes.

## Contributions & Thanks

These exercises are based on the Holberton School API curriculum. Contributions should keep the handlers small, explicit, and easy to test.