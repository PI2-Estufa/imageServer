import datetime 
from sqlalchemy import create_engine, Column, Integer, Unicode, Sequence, DateTime, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


engine = create_engine("postgresql://greenhouse:greenhouse@postgres:5432/greenhouse", echo=True)
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

class Image(Base):

    __tablename__ = 'image'

    id = Column(Integer, 
            Sequence('image_id_seq'), primary_key=True)
    url = Column(String)
    created_date = Column(DateTime, default=datetime.datetime.utcnow) 

Base.metadata.create_all(engine)
