from telethon.tl.functions.account import GetNotifySettingsRequest, UpdateNotifySettingsRequest, GetNotifyExceptionsRequest
from telethon.tl.types import InputPeerNotifySettings

from tg_api.client import client

async def get_peer_by_id(peer_id: int):
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