# AI-Powered Schema Selection for NL to SQL Pipelines

[cite_start]This project is a Python-based solution using the Django framework[cite: 3]. [cite_start]It allows users to convert natural language queries into relevant database schemas and SQL queries[cite: 4].

## 🚀 Features
* [cite_start]**NL to SQL Conversion**: Transforms natural language queries into functional SQL using AI (GPT-3.5-Turbo)[cite: 12, 16].
* [cite_start]**Schema Identification**: Automatically identifies relevant tables from the database[cite: 15].
* [cite_start]**Single API Endpoint**: Exposes one dedicated endpoint for processing queries[cite: 5, 18].
* [cite_start]**Local Execution**: Optimized for running on a local development server[cite: 7, 111].

---

## 📁 Project Structure
[cite_start]The project is organized into the following key files[cite: 37]:
* [cite_start]`urls.py`: Manages the API routes[cite: 39, 40].
* [cite_start]`views.py`: Contains the API logic to process NL queries[cite: 41, 42].
* [cite_start]`services.py`: Handles table selection and SQL generation[cite: 43, 44].
* [cite_start]`schema_loader.py`: Loads the database schema[cite: 45].
* [cite_start]`schema.json`: Stores database tables and column definitions[cite: 46, 47].

---

## 🛠️ Key Components
1. [cite_start]**QueryProcessor**: Extracts important words from the query and matches the best-fit database tables using Python libraries[cite: 49, 50, 51].
2. [cite_start]**SQLGenerator**: Uses GPT-3.5-Turbo to generate an SQL query based on the input query and relevant tables[cite: 52, 53, 54].

---

## ⚙️ Setup & Installation

### 1. Install Dependencies
[cite_start]Run the following commands to install the required packages and the Spacy model[cite: 56, 57, 58]:
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