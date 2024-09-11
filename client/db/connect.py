import os
from dotenv import load_dotenv
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

load_dotenv('.env')

dbname = os.getenv('DB_NAME')
dbuser = os.getenv('DB_USER')
dbpass = os.getenv('DB_PASSWORD')
dbhost = os.getenv('DB_HOST')

dbconnect = f"mysql+aiomysql://{dbuser}:{dbpass}@{dbhost}/{dbname}"
engine = create_async_engine(dbconnect)

AsyncSession = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)
session = AsyncSession()
