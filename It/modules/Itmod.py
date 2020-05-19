from sqlalchemy.orm import relation
from sqlalchemy import Column,Integer,String,DateTime,Boolean,Table,ForeignKey
import sys,os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from base.Basemod import BaseModule
from config.db import Base,session


class ItModoule(Base,BaseModule):
    pass
