import os
from dotenv import load_dotenv

load_dotenv()

api_key=os.getenv("API_KEY")
database_url=os.getenv("DATABASE_URL")

print(f"API_KEY:{api_key}")
print(f"DATABASE_URL:{database_url}")
