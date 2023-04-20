from dotenv import load_dotenv
import os

load_dotenv()
host = os.environ["MYSQL_HOST"] 
user = os.environ["MYSQL_USER"]
password = os.environ["MYSQL_PASSWORD"]
port = os.environ["MYSQL_PORT"]
database = os.environ["MYSQL_DATABASE"] 

DATABASE_CONNECTION_URI = f"mysql://{user}:{password}@{host}:{port}/{database}"

