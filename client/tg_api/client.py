import os

from dotenv import load_dotenv

from telethon import TelegramClient

load_dotenv()

api_id = os.getenv('API_ID')
api_hash = os.getenv('API_HASH')

# Initialize the Telegram client
client = TelegramClient('session_name', api_id, api_hash)
