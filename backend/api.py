from fastapi import FastAPI
from sqlalchemy import create_engine, text

app = FastAPI()

DATABASE_URL = "postgresql://username:password@localhost:5432/aqi_db"
engine = create_engine(DATABASE_URL)

@app.get("/aqi")
def get_aqi():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM aqi_data ORDER BY timestamp DESC LIMIT 10"))
        return {"data": [dict(row) for row in result]}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
