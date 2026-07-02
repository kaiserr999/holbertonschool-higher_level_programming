# Python Serialization

> Practice turning Python data into JSON, pickle, CSV, and XML, then reading it back.

## Description & Objectives

This project introduces the most common serialization formats used in Python. The tasks demonstrate how to persist dictionaries, lists, and structured data to files and how to reconstruct them later.

## Technologies Used

| Tool | Purpose |
| --- | --- |
| Python 3 | Main language for the exercises |
| `json` | JSON serialization and deserialization |
| `pickle` | Binary Python object serialization |
| `csv` | Comma-separated value export and import |
| `xml.etree.ElementTree` | XML generation and parsing |

## Prerequisites

- Python 3.10 or newer
- No external Python packages are required

## Installation

No installation step is needed. Clone the repository and change into the project folder.

```bash
cd python-serialization
```

## Usage

The modules can be imported from Python and called directly.

```bash
python3
```

```python
from task_00_basic_serialization import serialize_and_save_to_file, load_and_deserialize

payload = {"name": "Holberton", "year": 2026}
serialize_and_save_to_file(payload, "data.json")
print(load_and_deserialize("data.json"))
```

## Features

- JSON file writing and reading
- Pickle-based persistence
- CSV export helpers
- XML serialization and parsing

## Screenshots

No screenshots apply here; the project is validated by file contents and Python output.

## Documentation Standard

The modules use [PEP 257](https://peps.python.org/pep-0257/) docstrings for functions and helpers.

## Contributions & Thanks

Exercises inspired by the Holberton School Python curriculum. Contributions should preserve the simple, educational style of the tasks.