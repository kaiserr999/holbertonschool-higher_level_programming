# Holbertonschool Core Engineering

> Foundational Python exercises, environment demos, and learning notes for core engineering topics.

## Description & Objectives

This repository groups the early Python learning material used to practice control flow, virtual environment isolation, and formatted output. It serves as a small documentation-first project and a reference for the training workflow.

## Technologies Used

| Tool | Purpose |
| --- | --- |
| Python 3 | Exercises and environment demos |
| `venv` | Virtual environment isolation examples |
| Standard library modules | Random numbers, print formatting, and control flow |

## Prerequisites

- Python 3.10 or newer
- A POSIX-like shell or Windows terminal that can run Python commands
- No third-party packages are required for the included exercises

## Installation

No installation is needed. Clone the repository and move into the project folder.

```bash
cd holbertonschool-core-engineering
```

## Usage

Run the exercises directly from their folders:

```bash
python3 python_fundamentals/control_flow/positive_or_negative.py
python3 venv_isolation_demo.py
```

## Features

- Small Python exercises with clear output
- Virtual environment isolation demos
- Introductory control-flow practice
- Documentation-first organization

## Documentation Standard

Python files in this repository follow [PEP 257](https://peps.python.org/pep-0257/) docstrings for modules, functions, and classes.

## Contributions & Thanks

Built for Holberton School core engineering training. Thanks to the curriculum authors and reviewers.# Holbertonschool Core Engineering

A repository containing foundational Python programming exercises and learning materials for core engineering concepts.

## Project Structure

```
holbertonschool-core-engineering/
├── python_fundamentals/
│   ├── hello_world/
│   │   └── structured_output.py       # Formatted output, number classification, booleans, f-strings
│   └── control_flow/
│       └── positive_or_negative.py    # Control flow with if/elif/else
└── README.md
```

## Python Fundamentals

### Hello World - Structured Output

**File:** `python_fundamentals/hello_world/structured_output.py`

Demonstrates fundamental Python concepts:
- Formatted string output using f-strings
- Random number generation with `randint()`
- Numeric computation and float rounding
- Boolean logic and comparison operators
- Print statements with formatted output

**Output Example:**
```
Language: Python
Version: 3
Pi approx: 3.14
Computation valid: True
```

### Control Flow - Positive or Negative

**File:** `python_fundamentals/control_flow/positive_or_negative.py`

Exercises conditional logic and control flow:
- Random integer generation between -10 and 10
- if/elif/else decision structures
- F-string formatting for output
- Classification logic

**Output Examples:**
```
9 is positive
0 is zero
-2 is negative
```

## Requirements

- Python 3.10+
- No external dependencies (uses only built-in modules: `random`, `__import__`)

## Running the Exercises

### Structured Output
```bash
cd python_fundamentals/hello_world
python3 structured_output.py
```

### Positive or Negative
```bash
cd python_fundamentals/control_flow
python3 positive_or_negative.py
```

## Author

Created for Holbertonschool core engineering curriculum.

## License

All files in this repository are for educational purposes.
