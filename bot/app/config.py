import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("TOKEN")
ALL_BOOKS_URL = "http://localhost:8001/api/books/books/all"
