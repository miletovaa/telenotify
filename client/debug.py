from telethon.tl.types import User, Chat, Channel

def get_peer_title(Peer):
    if Peer.__class__ == User:
        return f'User: {Peer.first_name} {Peer.last_name if Peer.last_name is not None else ""}'
    elif Peer.__class__ == Chat:
        return f'Chat: {Peer.title}'
    elif Peer.__class__ == Channel:
        return f'Channel: {Peer.title}'
