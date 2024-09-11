import os

import asyncio

from config import settings
from db.controllers.mode import fetch_modes, is_mode_existent
from db.controllers.mode_peer import fetch_chats_by_mode
from db.controllers.exception import fetch_exception_chats

from tg_api.client import client
from tg_api.peer import get_peer_by_id, unmute_peer

from debug import get_peer_title


async def enable_mode(mode):
    # TODO: mute all chats
    if settings.debug:
        print("Enabling " + mode + " mode")

    exceptions = await fetch_exception_chats(client_id)

    by_mode = await fetch_chats_by_mode(client_id, mode)

    to_unmute = by_mode + exceptions

    for mode_peer in to_unmute:
        peer = await get_peer_by_id(mode_peer.peer_id)
        await unmute_peer(peer)
        
        if settings.debug:
            print(f"Unmuting {get_peer_title(peer)}")


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
        
        exit()


async def main():
    async with client as session:
        me = await session.get_me()
        global client_id
        client_id = me.id

        if settings.debug:
            print(f"Logged with {get_peer_title(me)}")

        await client.get_dialogs()

        await menu()

        await client.disconnect()

if __name__ == '__main__':
    asyncio.run(main())
