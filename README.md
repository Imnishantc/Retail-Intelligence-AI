
# Retail-Intelligence-AI

An AI-powered data analytics application that enables users to query a PostgreSQL database using natural language. The system converts user questions into SQL queries using a Large Language Model (Mistral AI), executes them on a retail sales database, and generates business insights along with visualizations.

---

## Project Overview

Traditional business analytics requires knowledge of SQL and database systems. This project simplifies data analysis by allowing users to ask business questions in plain English.

The application uses Mistral AI and LangChain to generate SQL queries, executes them on a PostgreSQL database containing retail transaction data, and returns meaningful insights through an interactive Streamlit dashboard.

Example:

**User Question**

> Which country generated the highest revenue?

**AI Workflow**

Natural Language → SQL Query → PostgreSQL Execution → Business Insight → Visualization

---

## Architecture

```text
User Question
      ↓
Streamlit Dashboard
      ↓
Mistral AI + LangChain
      ↓
SQL Query Generation
      ↓
PostgreSQL Database
      ↓
Query Execution
      ↓
Results
      ↓
Business Insight Generation
      ↓
Data Visualization
```

---

## Features

* Natural Language to SQL Conversion
* PostgreSQL Database Integration
* AI-Powered Business Insight Generation
* Interactive Streamlit Dashboard
* Automatic Data Visualization
* Revenue Analysis and Customer Analytics
* Modular Project Structure
* Environment Variable Management using .env

---

## Tech Stack

### Programming Language

* Python

### Database

* PostgreSQL

### AI / LLM

* Mistral AI
* LangChain

### Data Processing

* Pandas
* NumPy

### Visualization

* Matplotlib
* Streamlit

### Development Tools

* VS Code
* Git & GitHub

---

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
│   └── prompts.py
│
├── data/
│   └── online_retail.csv
│
├── database/
│   └── load_data.py
│
├── requirements.txt
├── README.md
└── .env
```

---

## Installation

### Clone Repository

```bash
git clone <repository-url>
cd AI-SQL-Analyst
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

Windows:

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Configure Environment Variables

Create a `.env` file:

```env
MISTRAL_API_KEY=your_api_key
```

### Run Streamlit Application

```bash
streamlit run app/streamlit_app.py
```

---

## Sample Questions

* Which country generated the highest revenue?
* Show top 10 countries by revenue.
* Show top 5 customers by revenue.
* Which products generated the highest sales?
* What is the average revenue per customer?

---

## Screenshots

### Dashboard
<img width="1912" height="920" alt="image" src="https://github.com/user-attachments/assets/8dad631b-588d-49e3-baeb-a18e3b00b6ca" />


### Generated SQL

<img width="1903" height="565" alt="image" src="https://github.com/user-attachments/assets/84bb498c-729c-48bb-84eb-4cdb556d70a4" />

<img width="1907" height="365" alt="image" src="https://github.com/user-attachments/assets/b643beff-21af-4e75-a57b-fc30e89f2ade" />

### Business Insights

<img width="1817" height="270" alt="image" src="https://github.com/user-attachments/assets/e86eb108-d4a5-4a63-852f-525b64df82b8" />


### Visualization

<img width="1807" height="515" alt="image" src="https://github.com/user-attachments/assets/63495a0e-421e-4b5d-9d9a-8bfc54268fe6" />

---

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
* Docker Containerization
* Cloud Deployment
* Advanced Analytics Dashboard
* Role-Based Access Control

---

## Author

Nishant Chavan

B.Tech Electronics & Telecommunication Engineering


>>>>>>> ea8b6e94fa8dcee62ff7da4977285998a03626a5
