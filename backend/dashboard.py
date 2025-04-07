import streamlit as st
import pandas as pd
from sqlalchemy import create_engine, text

# ตั้งค่าการเชื่อมต่อฐานข้อมูล
DATABASE_URL = "postgresql://username:password@localhost:5432/aqi_db"
engine = create_engine(DATABASE_URL)

# ดึงข้อมูลจากฐานข้อมูล
def load_data():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM aqi_data ORDER BY timestamp DESC LIMIT 50"))
        df = pd.DataFrame(result.fetchall(), columns=result.keys())
    return df

# เริ่มต้น Streamlit Dashboard
st.set_page_config(page_title="AQI Dashboard", layout="wide")

st.title("🌍 AQI Dashboard - Bangkok")

# โหลดข้อมูล
df = load_data()

# แสดงค่า AQI ล่าสุด
st.metric(label="AQI ปัจจุบัน", value=df.iloc[0]["aqi"])

# แสดงกราฟ AQI
st.subheader("📊 ค่า AQI ล่าสุด")
st.line_chart(df.set_index("timestamp")["aqi"])

# แสดงค่า PM2.5
st.subheader("🛑 ค่า PM2.5 ล่าสุด")
st.line_chart(df.set_index("timestamp")["pm25"])

# ตารางข้อมูลล่าสุด
st.subheader("📋 ข้อมูล AQI ล่าสุด")
st.dataframe(df)
