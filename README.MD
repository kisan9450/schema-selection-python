# AI-Powered Schema Selection for NL to SQL Pipelines

This project is a Python-based solution using the Django framework. It allows users to convert natural language queries into relevant database schemas and SQL queries.

## 🚀 Features
* **NL to SQL Conversion**: Transforms natural language queries into functional SQL using AI (GPT-3.5-Turbo).
* **Schema Identification**: Automatically identifies relevant tables from the database.
* **Single API Endpoint**: Exposes one dedicated endpoint for processing queries.
* **Local Execution**: Optimized for running on a local development server.

---

## 📁 Project Structure
The project is organized into the following key files:
* `urls.py`: Manages the API routes.
* `views.py`: Contains the API logic to process NL queries.
* `services.py`: Handles table selection and SQL generation.
* `schema_loader.py`: Loads the database schema.
* `schema.json`: Stores database tables and column definitions.

---

## 🛠️ Key Components
1. **QueryProcessor**: Extracts important words from the query and matches the best-fit database tables using Python libraries.
2. **SQLGenerator**: Uses GPT-3.5-Turbo to generate an SQL query based on the input query and relevant tables.

---

## ⚙️ Setup & Installation

### 1. Install Dependencies
Run the following commands to install the required packages and the Spacy model:
```bash
pip install django openai spacy sentence-transformers
python -m spacy download en_core_web_sm


2. Run the Project
Start the Django development server:
python manage.py runserver

The server will start at http://127.0.0.1:8000/


📡 API Documentation
Convert Natural Language to SQL

Endpoint: /api/nl-to-sql/ 


Method: POST 


Description: Converts a natural language query into an SQL query.

Request Format 

Body (JSON):


{
  "query": "Show me all employees who joined in 2024"
}


Response Format 

Status: 200 OK

{
  "natural_query": "Show me all employees who joined in 2024",
  "relevant_tables": [
    {
      "name": "employees",
      "columns": ["id", "name", "email", "hire_date"]
    }
  ],
  "sql_query": "SELECT * FROM employees WHERE hire_date >= '2024-01-01';"
}


For more detail refer assignment-solution.pdf file
