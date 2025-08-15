## Overview

This project is a fully Dockerized data pipeline built using Apache Airflow.
It automatically fetches stock market data from a free API (Alpha Vantage) and stores the data into a PostgreSQL database — all inside Docker.

You can run the entire setup using just one command.

# What This Project Does

1. Fetches stock prices (like IBM) from Alpha Vantage API daily

2. Parses and cleans the JSON data

3. Stores it into PostgreSQL using safe insert logic (no duplicates)

4. Scheduled daily using Airflow

5. Uses .env to keep API keys and passwords safe

6. Fully runs inside Docker using docker compose up

stock_pipeline_project/
│
├── dags/
│   ├── stock_data_dag.py       # Airflow DAG
│   └── fetch_and_store.py      # Python script for fetching + inserting data
│
├── .env                        # Contains API key and DB credentials
├── docker-compose.yml          # Sets up Airflow + PostgreSQL
├── requirements.txt            # Python dependencies


## How to Run This Project

1. Clone the repo and go inside
git clone <repo_url>
cd stock_pipeline_project

2. Add your .env file
STOCK_API_KEY=your_api_key_here
POSTGRES_USER=stock
POSTGRES_PASSWORD=qwert1234
POSTGRES_DB=stocks_db

3. Run the full setup
docker compose up --build

4. Open Airflow

Go to → http://localhost:8080

Login:

Username: *****

Password: *****

Trigger the DAG manually (▶️ icon)

# Technologies Used

Apache Airflow (in Docker)

PostgreSQL (in Docker)

Python (requests, psycopg2)

Docker Compose

Alpha Vantage API