import os
from sqlalchemy import create_engine
from dotenv import load_dotenv

load_dotenv()

try:
    url = os.getenv("DATABASE_URL")
    print(f"Testing URL: {url.split('@')[1] if '@' in url else '...'}") # hide credentials
    engine = create_engine(url)
    connection = engine.connect()
    print("Successfully connected to the database!")
    connection.close()
except Exception as e:
    print(f"Error connecting: {e}")
