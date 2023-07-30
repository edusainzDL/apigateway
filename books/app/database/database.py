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
        return cls.__instances[cls]

class Database(metaclass=SingletonMeta):

    Base                    = declarative_base()
    session: sessionmaker   = None
    engine = None

    def __init__(self) -> None:
        self.engine = create_engine(
            settings.DATABASE_URL,
            isolation_level = 'AUTOCOMMIT',
            pool_use_lifo=True
        )

        self.Base.metadata.create_all(self.engine)
    
    def get_db_session(self):
        if self.session is None:
            self.session = sessionmaker(bind=self.engine, future=True)
            self.session = self.session()
        return self.session