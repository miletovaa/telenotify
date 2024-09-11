import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

load_dotenv()

dbname = os.getenv('DB_NAME')
dbuser = os.getenv('DB_USER')
dbpass = os.getenv('DB_PASSWORD')
dbserver = os.getenv('DB_SERVER')

dbconnect = f"mysql+pymysql://{dbuser}:{dbpass}@{dbserver}/{dbname}"
engine = create_engine(dbconnect)

Session = sessionmaker(bind=engine)
session = Session()