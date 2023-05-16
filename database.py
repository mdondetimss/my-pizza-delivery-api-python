from  sqlalchemy import create_engine
from  sqlalchemy.orm import declarative_base,sessionmaker
from urllib import parse

password=parse.quote('mydb786')
engine=create_engine('postgresql://postgres:mydb%40786@localhost/pizza_delivery',
    echo=True
  
)

Base = declarative_base()
Session = sessionmaker()

