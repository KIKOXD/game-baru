# Kymang

import os
from dotenv import load_dotenv

load_dotenv(".env")  # Load dari file .env

BOT_TOKEN = os.environ["BOT_TOKEN"]
API_ID = int(os.environ["API_ID"])
API_HASH = os.environ["API_HASH"]
MONGO_URL = os.environ["MONGO_URL"]
ADMINS = [int(x) for x in os.environ["ADMINS"].split()]
MEMBER = [int(x) for x in os.environ["MEMBER"].split()]
LOG_GRP = int(os.environ["LOG_GRP"])
BOT_ID = int(os.environ["BOT_ID"])
KITA = [int(x) for x in os.environ["KITA"].split()]
