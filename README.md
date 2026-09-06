# Financial Transaction ETL Pipeline

A hands-on Python ETL project for processing financial transaction data with validation, cleaning, transformation, and structured outputs.

This project is part of my learning journey toward Python Data Engineering, Pandas, PySpark, PostgreSQL, and Azure Data Lake.

## Project Goal

The goal is to learn Python by building a practical ETL pipeline using financial transaction data.

The pipeline will gradually evolve from a simple CSV processor into a more complete data engineering project.

## Current Flow

```text
transactions.csv
       |
       v
    Extract
       |
       v
    Validate
       |
       v
   Transform
       |
   +---+---+
   |       |
   v       v
 Valid   Rejected
```

## Current Features

* Read transaction data from CSV
* Convert and process transaction values
* Validate transaction amounts
* Identify invalid transaction records

## Planned Improvements

* Duplicate transaction detection
* Missing field validation
* Clean and rejected CSV outputs
* Python classes and better project structure
* Exception handling
* Logging
* Automated tests with pytest
* PostgreSQL integration
* Pandas implementation
* PySpark processing
* Azure Data Lake integration

## Tech Stack

* Python
* CSV

More technologies will be added as the project evolves.

## Run the Project

Create a virtual environment:

```bash
py -m venv .venv
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

Run the application:

```bash
python main.py
```

## Learning Roadmap

```text
Python
  ↓
ETL
  ↓
Pandas
  ↓
PostgreSQL
  ↓
PySpark
  ↓
Azure Data Lake
```

## Status

🚧 Currently under development and being expanded as part of my Python and Data Engineering learning journey.
