from db.connect import AsyncSession
from db.models import ModePeer, Mode
from sqlalchemy.future import select

async def fetch_modes(client_id):
    async with AsyncSession() as session:
        response = await session.execute((
            select(Mode)
            .join(ModePeer)
            .filter(ModePeer.client_id == client_id)
            .group_by(Mode.id)
        ))
        return response.scalars().all()

async def is_mode_existent(client_id, mode):
    async with AsyncSession() as session:
        response = await session.execute((
            select(Mode)
            .join(ModePeer)
            .filter(ModePeer.client_id == client_id)
            .filter(Mode.name == mode)
        ))
        return response.scalars().first() is not None
