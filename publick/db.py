'''
the data config
'''
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from load import LoadYaml


class DbError(Exception):
    pass

db_config = LoadYaml.load().get("database",'')
print(db_config)
if not db_config:
    raise DbError("can not find database config")

db_url = 'mysql+pymysql://{}:{}@{}/{}?charset=utf8'.format(
    db_config.get('username'),
    db_config.get('passport'),
    db_config.get('hostname'),
    db_config.get('database'),
)

engine = create_engine(db_url)
Base = declarative_base(engine)

Session = sessionmaker(engine)
session = Session()