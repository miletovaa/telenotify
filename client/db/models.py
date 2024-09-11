from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Mode(Base):
    __tablename__ = 'modes'
    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    is_default = Column(Boolean, default=False)

    mode_peers = relationship('ModePeer', back_populates='mode')

    def __str__(self):
        return self.name

class ModePeer(Base):
    __tablename__ = 'mode_peers'

    id = Column(Integer, primary_key=True)
    client_id = Column(Integer)
    mode_id = Column(Integer, ForeignKey('modes.id'))
    peer_id = Column(Integer)

    mode = relationship('Mode', back_populates='mode_peers')

    def __str__(self):
        return f'{self.mode.name}: {self.peer_id}'

class ClientException(Base):
    __tablename__ = 'client_exceptions'

    client_id = Column(Integer, primary_key=True)
    peer_id = Column(Integer)

    def __str__(self):
        return self.peer_id
