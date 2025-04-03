import requests
import json
from datetime import datetime
from sqlalchemy import create_engine

# ตั้งค่า API
API_KEY = "09b90895-d92b-42e0-8492-500158c9950a"
URL = f"https://api.airvisual.com/v2/city?city=Bangkok&state=Bangkok&country=Thailand&key={API_KEY}"

# ดึงข้อมูลจาก API
def fetch_aqi_data():
    response = requests.get(URL)
    data = response.json()
    if "data" in data:
        city = data["data"]["city"]
        aqi = data["data"]["current"]["pollution"]["aqius"]
        pm25 = data["data"]["current"]["pollution"]["pm25"]
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return city, aqi, pm25, timestamp
    return None

# บันทึกข้อมูลลง PostgreSQL
def save_to_db(city, aqi, pm25, timestamp):
    DATABASE_URL = "postgresql://username:password@localhost:5432/aqi_db"
    engine = create_engine(DATABASE_URL)
    with engine.connect() as conn:
        conn.execute(f"""
            INSERT INTO aqi_data (city, aqi, pm25, timestamp)
            VALUES ('{city}', {aqi}, {pm25}, '{timestamp}');
        """)

if __name__ == "__main__":
    data = fetch_aqi_data()
    if data:
        save_to_db(*data)


import time

while True:
    data = fetch_aqi_data()
    if data:
        save_to_db(*data)
    time.sleep(300)  # ดึงข้อมูลทุก 5 นาที
