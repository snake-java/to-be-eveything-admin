from sqlalchemy.orm import relation
from sqlalchemy import Column,Integer,String,DateTime,Boolean,Table,ForeignKey
import sys,os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from publick.base.Basemod import BaseModule
from publick.db import Base,session


class ItModoule(Base,BaseModule):
    pass
