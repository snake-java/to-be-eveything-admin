from datetime import datetime
from sqlalchemy import Column,Integer,String,DateTime

class BaseModule():
    yn = Column(Integer,default=1,nullable=False)
    create_time = Column(DateTime,default=datetime.now)
    modify_time= Column(DateTime,default=datetime.now)