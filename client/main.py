from telethon import TelegramClient
from telethon.tl.functions.account import GetNotifySettingsRequest, UpdateNotifySettingsRequest, GetNotifyExceptionsRequest
from telethon.tl.types import InputPeerNotifySettings
from dotenv import load_dotenv
import asyncio
import os

# File with an object of temporary modes. This we will fetch from the DB. Peer_ids are the only chats that will not be muted when the mode is enabled
import modes 

# Load environment variables from .env file
load_dotenv()

# Get API credentials from environment variables
api_id = os.getenv('API_ID')
api_hash = os.getenv('API_HASH')
phone = os.getenv('PHONE')

# Initialize the Telegram client
client = TelegramClient('session_name', api_id, api_hash)

print(modes.modes)

async def get_user_by_peer_id(peer_id: int):
    async with client:
        # Try to fetch the user by their peer ID
        try:
            user = await client.get_entity(peer_id)
            return user
        except Exception as e:
            print(f"Error fetching user by peer ID: {e}")
            return None
        
async def update_notification_settings(user_peer, mute_until):
    async with client:
        # Update the notification settings using UpdateNotifySettingsRequest
        try:
            notify_settings = InputPeerNotifySettings(mute_until=mute_until)
            result = await client(UpdateNotifySettingsRequest(peer=user_peer, settings=notify_settings))
            return result
        except Exception as e:
            print(f"Error updating notification settings: {e}")
            return None
        
async def fetch_mode_chats(mode):
    # get chats from the DB based on the mode
    print(f"Fetching {mode} chats from the database")

async def fetch_exception_chats(mode):
    # get chats that are never muted from the DB
    print("Fetching exception chats from the database")
    return modes[mode] # temporary return
        
async def enable_mode(mode):
    # get exceptions and merge them with modes[mode]
    exceptions = await fetch_exception_chats()
    mode = await fetch_mode_chats(mode)
    mode_exceptions = mode + exceptions
    # mute all chats
    # set notification exceptions
        
# async def get_notify_exceptions():
#     async with client:
#         try:
#             notify_settings = await client(GetNotifyExceptionsRequest())
#             return notify_settings
#         except Exception as e:
#             print(f"Error fetching notification settings: {e}")
#             return None

async def main():
    async with client as session:
        me = await session.get_me()
        print(f"This is me: {me.first_name} {me.last_name if not 'None' else ''}")

        while True:
            print("\nCommand Menu")
            print("/general")
            print("/work")
            print("/personal")
            print("/setexceptions")

            choice = input("Insert command: ")

            if choice == '/general':
                enable_mode('general')
            elif choice == '/work':
                enable_mode('work')
            elif choice == '/personal':
                enable_mode('personal')
                break
            else:
                print("Invalid command, please try again.")

        await client.disconnect()

# Run the script
if __name__ == '__main__':
    asyncio.run(main())
