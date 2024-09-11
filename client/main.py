from db.controllers.mode import fetch_modes, is_mode_existent
from db.controllers.mode_peer import fetch_chats_by_mode
from db.controllers.exception import fetch_exception_chats

from telethon import TelegramClient
from telethon.tl.functions.account import GetNotifySettingsRequest, UpdateNotifySettingsRequest, GetNotifyExceptionsRequest
from telethon.tl.types import InputPeerNotifySettings

from dotenv import load_dotenv
import asyncio
import os

load_dotenv()

api_id = os.getenv('API_ID')
api_hash = os.getenv('API_HASH')

debug = os.getenv('DEBUG')

# Initialize the Telegram client
client = TelegramClient('session_name', api_id, api_hash)

async def get_user_by_peer_id(peer_id: int):
    async with client:
        try:
            user = await client.get_entity(peer_id)
            return user
        except Exception as e:
            print(f"Error fetching user by peer ID: {e}")
            return None
        
async def unmute_peer(peer):
    async with client:
        try:
            notify_settings = InputPeerNotifySettings(mute_until=0)
            result = await client(UpdateNotifySettingsRequest(peer=peer, settings=notify_settings))
            return result
        except Exception as e:
            print(f"Error updating notification settings: {e}")
            return None

async def enable_mode(mode):
    # TODO: mute all chats
    print("Enabling " + mode + " mode")

    exceptions = await fetch_exception_chats(client_id)

    by_mode = await fetch_chats_by_mode(client_id, mode)

    to_unmute = by_mode + exceptions

    for mode_peer in to_unmute:
        peer = await get_user_by_peer_id(mode_peer.peer_id)
        print(peer)
        await unmute_peer(peer)
        print(peer)
        print(" is unmuted")

async def get_menu_options():
    available_modes = await fetch_modes(client_id)

    commands = list(map(lambda x: x.name, available_modes))
    commands.append('setexceptions')
    return commands

async def menu():
    options = await get_menu_options()

    while True:
        print("\nCommand Menu")
        for option in options:
            print(f"/{option}")

        command = input("Insert command: ")

        if command == '/setexceptions':
            print("Setting exceptions")
        else:
            does_mode_exist = await is_mode_existent(client_id, command[1:])

            if does_mode_exist:
                await enable_mode(command[1:])
            else:
                print("\nInvalid command, please try again.")
        
        break


async def main():
    async with client as session:
        me = await session.get_me()
        global client_id
        client_id = me.id

        await client.get_dialogs()

        await menu()

        await client.disconnect()

if __name__ == '__main__':
    asyncio.run(main())
