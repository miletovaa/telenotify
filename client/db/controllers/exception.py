from db.connect import AsyncSession
from db.models import ClientException
from sqlalchemy.future import select

async def fetch_exception_chats(client_id):
    async with AsyncSession() as session:
        response = await session.execute((
            select(ClientException)
            .filter(ClientException.client_id == client_id)
        ))
        return response.scalars().all()