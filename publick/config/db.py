from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


HOSTNAME = '10.0.0.200'
PROT = '3306'
DATABASE = 'db_wxprogram'
USERNAME = 'root'
PASSWORD = 'qwe123'

db_url = 'mysql+pymysql://{}:{}@{}/{}?charset=utf8'.format(
    USERNAME,
    PASSWORD,
    HOSTNAME,
    DATABASE
)

engine = create_engine(db_url)
Base = declarative_base(engine)

Session = sessionmaker(engine)
session = Session()