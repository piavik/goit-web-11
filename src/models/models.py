from sqlalchemy import Integer, Column, String, Date
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Contact(Base):
    __tablename__ = "contacts"
    id       = Column(Integer, primary_key=True)
    name     = Column('name', String(50), nullable=False)
    surname  = Column('surname', String(50), nullable=False)
    email    = Column('email', String(100), unique=True, nullable=False)
    phone    = Column('phone', String(15), unique=True, nullable=False)
    birthday = Column('phone', Date, nullable=False)
    notes    = Column('notes', String, nullable=True)
