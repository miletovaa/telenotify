from dbconnect import session
from models import ClientMode, Mode

client_id = your_client_id

def fetch_modes():
    return session.query(Mode).join(ClientMode).filter(ClientMode.client_id == client_id).all()

def fetch_chats_by_mode(mode):
    if isinstance(mode, Mode):
        return session.query(ClientMode).filter(ClientMode.mode_id == mode.id).first().chats
    elif type(mode) == int:
        return session.query(ClientMode).filter(ClientMode.mode_id == mode).first().chats
    else:
        return session.query(ClientMode).join(Mode).filter(Mode.name == mode).first().chats
