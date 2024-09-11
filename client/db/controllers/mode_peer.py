from db.connect import AsyncSession
from db.models import ModePeer, Mode
from sqlalchemy.future import select

async def fetch_chats_by_mode(client_id, mode):
    async with AsyncSession() as session:
        response = await session.execute((
            select(ModePeer)
            .join(Mode)
            .filter(ModePeer.client_id == client_id)
            .filter(Mode.name == mode)
        ))
        return response.scalars().all()

    # if isinstance(mode, Mode):
    #     return await session.query(ModePeer).filter(ModePeer.mode_id == mode.id).first().chats
    # elif type(mode) == int:
    #     return await session.query(ModePeer).filter(ModePeer.mode_id == mode).first().chats
    # else:
    #     return await session.query(ModePeer).join(Mode).filter(Mode.name == mode).first().chats
