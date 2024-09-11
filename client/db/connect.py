from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

from config import settings

dbconnect = f"mysql+aiomysql://{settings.db_user}:{settings.db_password}@{settings.db_host}/{settings.db_name}"
engine = create_async_engine(dbconnect)

AsyncSession = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)
session = AsyncSession()
