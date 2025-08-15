from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from fetch_and_store import fetch_and_store_stock_data

# Add scripts directory to path
sys.path.append(os.path.join(os.path.dirname(__file__), '../scripts'))
from fetch_and_store import fetch_and_store_stock_data

default_args = {
    'owner': 'airflow',
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
    dag_id='fetch_stock_data_daily',
    default_args=default_args,
    description='Fetch stock data and store in PostgreSQL daily',
    schedule_interval='@daily',
    start_date=datetime(2023, 1, 1),
    catchup=False
) as dag:
    
    fetch_and_store = PythonOperator(
        task_id='fetch_and_store_task',
        python_callable=fetch_and_store_stock_data
    )
    
    fetch_and_store
