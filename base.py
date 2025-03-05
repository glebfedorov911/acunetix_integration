import os

from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv('BASE_URL')
TARGET_API_URL = os.getenv('TARGET_API_URL')
API_KEY = os.getenv("API_KEY")