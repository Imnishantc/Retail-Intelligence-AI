
# Retail-Intelligence-AI

An end-to-end AI-powered Business Intelligence application that enables users to interact with a PostgreSQL database using natural language. The system leverages Mistral AI and LangChain to convert business questions into SQL queries, execute them on a retail sales database, generate business insights, and visualize results through an interactive Streamlit dashboard.

## Key Highlights

- Natural Language → SQL Query Generation using Mistral AI
- AI-Powered Business Insight Generation
- PostgreSQL Database Integration
- Interactive Streamlit Dashboard
- Automated Data Visualization
- Dockerized Deployment
- Modular and Scalable Architecture


## Project Overview

Traditional business analytics requires knowledge of SQL and database systems. This project simplifies data analysis by allowing users to ask business questions in plain English.

The application uses Mistral AI and LangChain to generate SQL queries, executes them on a PostgreSQL database containing retail transaction data, and returns meaningful insights through an interactive Streamlit dashboard.

Example:

**User Question**

> Which country generated the highest revenue?

**AI Workflow**

Natural Language → SQL Query → PostgreSQL Execution → Business Insight → Visualization

---

## Docker Support

Build Docker Image

```bash
docker build -t retail-intelligence-ai .
```

Run Docker Container

```bash
docker run -p 8501:8501 --env-file .env retail-intelligence-ai
```

The application will be available at:

http://localhost:8501

## Architecture

<img width="610" height="908" alt="image" src="https://github.com/user-attachments/assets/2ea7125e-2951-4219-863c-eb82b91f512a" />

## Features

- Natural Language to SQL Conversion using Mistral AI
- PostgreSQL Database Integration
- AI-Powered Business Insight Generation
- Interactive Streamlit Dashboard
- Automatic Data Visualization with Matplotlib
- Dynamic SQL Query Generation
- Revenue Analysis and Customer Analytics
- Retail Sales Performance Reporting
- Prompt Engineering for Accurate SQL Generation
- Docker Containerization
- Modular and Scalable Project Architecture
- Environment Variable Management using .env

## Tech Stack

### Programming Language

- Python

### Database

- PostgreSQL
- SQLAlchemy

### AI / LLM

- Mistral AI
- LangChain
- Prompt Engineering

### Data Processing

- Pandas
- NumPy

### Visualization & Dashboard

- Matplotlib
- Streamlit

### DevOps & Deployment

- Docker

### Development Tools

- VS Code
- Git
- GitHub

  
## Dataset

The project uses the Online Retail Dataset containing over 400,000 retail transactions.

Dataset includes:

* Invoice Information
* Product Information
* Customer Information
* Country Information
* Revenue Data

Additional revenue features were engineered during data preprocessing.

---

## Project Structure

```text
Retail-Intelligence-AI/
│
├── app/
│   ├── streamlit_app.py
│   ├── sql_agent.py
│   ├── query_executor.py
│   ├── explanation_generator.py
│   ├── chart_generator.py
│   ├── prompts.py
│   └── test_mistral.py
│
├── data/
│   ├── cleaned_retail_sales.csv
│   └── online_retail_II.xlsx
│
├── database/
│   ├── create_tables.sql
│   ├── db_connection.py
│   └── load_data.py
│
├── notebooks/
│   └── data_cleaning.ipynb
│
├── Dockerfile
├── .dockerignore
├── requirements.txt
├── README.md
└── .env
```


## Sample Questions

* Which country generated the highest revenue?
* Show top 10 countries by revenue.
* Show top 5 customers by revenue.
* Which products generated the highest sales?
* What is the average revenue per customer?

---

## Screenshots

### Dashboard
<img width="1917" height="930" alt="image" src="https://github.com/user-attachments/assets/30e624bb-337e-43c2-8368-493037e1ec58" />


### Generated SQL

<img width="1913" height="775" alt="image" src="https://github.com/user-attachments/assets/1d6b86a7-d4e8-4419-96e5-32319ba2b019" />

<img width="1916" height="745" alt="image" src="https://github.com/user-attachments/assets/49469f9e-d629-4e3d-a49c-66ec14cae497" />


### Business Insights

<img width="1906" height="337" alt="image" src="https://github.com/user-attachments/assets/574a804c-2d08-4d7c-b306-603cd2e26d8a" />



### Visualization

<img width="1917" height="781" alt="image" src="https://github.com/user-attachments/assets/bd8f51cd-10e9-4807-8de1-d2eb89b9b263" />


### Docker container running

<img width="1593" height="626" alt="image" src="https://github.com/user-attachments/assets/4b4dc029-0864-4a60-93fb-2d249cad9b5b" />



## Real-World Applications

This project can be used by:

- Retail companies for sales analysis
- Business analysts for quick reporting
- Non-technical managers who do not know SQL
- E-commerce platforms for revenue monitoring
- Data teams for self-service analytics

The system reduces dependency on SQL expertise by allowing users to interact with databases using natural language.


## Learning Outcomes

Through this project I gained hands-on experience in:

* Large Language Models (LLMs)
* Prompt Engineering
* LangChain Framework
* PostgreSQL Database Management
* Natural Language Query Processing
* Data Visualization
* Streamlit Application Development
* End-to-End AI Application Development

---

## Future Enhancements

* Query History Tracking
* Download Results as CSV
* Multi-Database Support
* User Authentication
* Cloud Deployment
* Advanced Analytics Dashboard
* Role-Based Access Control

---

## Author

Nishant Chavan

B.Tech Electronics & Telecommunication Engineering
