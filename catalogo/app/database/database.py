from typing import Any
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.core.settings import settings

class SingletonMeta(type):
    __instances = {}

    def __call__(cls,*args, **kwargs) -> Any:
        if cls not in cls.__instances:
            instance = super().__call__(*args, **kwargs)
            cls.__instances[cls] = instance
        return cls.__instances

class Database(metaclass=SingletonMeta):

    Base                    = declarative_base()
    session: sessionmaker   = None

    def __init__(self) -> None:
        self.__engine = create_engine(
            settings.DATABASE_URL
        )

        self.Base.metadata.create_all(self.__engine)
    
    def get_db_session(self):
        if self.session is None:
            self.session = sessionmaker(base=self.__engine, future=True)
            self.session = self.session()
        return self.session