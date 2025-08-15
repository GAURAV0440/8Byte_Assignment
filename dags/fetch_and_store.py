import os
import requests
import psycopg2

def fetch_and_store_stock_data():
    api_key = os.getenv('STOCK_API_KEY')
    symbol = 'IBM'
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={api_key}'
    
    response = requests.get(url)
    data = response.json()
    
    # Extract the most recent day's data
    daily_data = data['Time Series (Daily)']
    latest_date = sorted(daily_data.keys())[-1]
    latest_close = daily_data[latest_date]['4. close']
    
    # Connect to PostgreSQL
    conn = psycopg2.connect(
        host='postgres_db',
        database=os.getenv('POSTGRES_DB'),
        user=os.getenv('POSTGRES_USER'),
        password=os.getenv('POSTGRES_PASSWORD')
    )
    cur = conn.cursor()
    
    cur.execute("""
        CREATE TABLE IF NOT EXISTS stock_prices (
            date TEXT PRIMARY KEY,
            close_price FLOAT
        );
    """)
    
    cur.execute("""
        INSERT INTO stock_prices (date, close_price)
        VALUES (%s, %s)
        ON CONFLICT (date) DO UPDATE SET close_price = EXCLUDED.close_price;
    """, (latest_date, latest_close))

    conn.commit()
    cur.close()
    conn.close()
