# Python Object-Relational Mapping

> Learn how to connect Python to MySQL and model tables with SQLAlchemy.

## Description & Objectives

This project covers direct MySQL access with `MySQLdb` and object-relational mapping with SQLAlchemy. The exercises focus on querying, filtering, inserting, updating, deleting, and modeling database rows in Python.

## Technologies Used

| Tool | Purpose |
| --- | --- |
| Python 3 | Language used for the scripts and models |
| MySQL / MariaDB | Database engine used by the exercises |
| MySQLdb / mysqlclient | Low-level database access |
| SQLAlchemy | ORM layer and model definitions |

## Prerequisites

- Python 3.10 or newer
- MySQL Server running locally
- A user with access to the `hbtn_0e_0_usa` database or the database specified by the task
- Python packages such as `mysqlclient` and `SQLAlchemy`

## Installation

Create a virtual environment and install the required packages:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install mysqlclient SQLAlchemy
```

Depending on your platform, you may also need MySQL development headers before installing `mysqlclient`.

## Usage

Run the scripts with the MySQL credentials expected by each task.

```bash
python3 0-select_states.py user password database_name
python3 10-model_state_my_get.py user password database_name
```

Example output:

```text
(1, 'California')
(2, 'Texas')
```

## Features

- Raw SQL queries against MySQL tables
- Safe parameter handling for user input
- SQLAlchemy model definitions for states and cities
- ORM exercises covering fetch, insert, update, delete, and relationships

## Screenshots

No screenshots are included; the exercises are validated through terminal output.

## Documentation Standard

The Python files follow [PEP 257](https://peps.python.org/pep-0257/) docstrings for modules, functions, and classes.

## Contributions & Thanks

Based on the Holberton School database curriculum. Thanks to the maintainers and reviewers who shaped the exercise sequence.
