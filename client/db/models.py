from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Mode(Base):
    __tablename__ = 'modes'
    id = Column(Integer, primary_key=True)
    name = Column(String(255))

    client_modes = relationship('ClientMode', back_populates='mode')

    def __str__(self):
        return self.name

class ClientMode(Base):
    __tablename__ = 'client_modes'

    client_id = Column(Integer, primary_key=True)
    mode_id = Column(Integer, ForeignKey('modes.id'), primary_key=True)
    chats = Column(String(255))

    mode = relationship('Mode', back_populates='client_modes')
