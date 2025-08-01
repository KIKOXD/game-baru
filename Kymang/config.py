#Kymang

import os

from dotenv import load_dotenv

load_dotenv(".env")


BOT_TOKEN = os.environ.get("BOT_TOKEN", "8428504928:AAFrKOnlIkyU83RnGQsZbYXDjTkz2z8r9kc")
API_ID = int(os.environ.get("API_ID", "27538621"))
API_HASH = os.environ.get("API_HASH", "24c338d23154f5ea8adb9fc684a4a06f")
MONGO_URL = os.environ.get("MONGO_URL", "mongodb+srv://baskara:123@cluster0.83cht0e.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
ADMINS = [int(x) for x in (os.environ.get("ADMINS", "478043396").split())]
MEMBER = [int(x) for x in (os.environ.get("MEMBER", "600").split())]
LOG_GRP = int(os.environ.get("LOG_GRP", "-1002288511799"))
BOT_ID = int(os.environ.get("BOT_ID", "8428504928"))

KITA = [int(x) for x in (os.environ.get("KITA", "478043396").split())]
