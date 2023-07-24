from app.api.books.domain.create import Create
from app.api.books.domain.get_all import GetAll
from app.api.books.domain.get_id import GetId
from app.api.books.domain.update import Update
from app.api.books.domain.delete import Delete
from app.core.errors import responses as errors
from app.api.books.schema import (
    BookCreate,
    BookPath,
    BookResponse,
    BookResponseAll
)
from uuid import UUID
class Controller:
    @staticmethod
    def create(book:BookCreate):
        try:
            return Create().execute(book)
        except RuntimeError as exec:
            return errors[exec.err_type]
        except Exception as exec:
            return errors['ERROR_SERVER']
        
    @staticmethod
    def get_all():
        try:
            return GetAll().execute()
        except RuntimeError as exec:
            return errors[exec.err_type]
        except Exception as exec:
            return errors['ERROR_SERVER']
    @staticmethod
    def get_id(book_id:UUID):
        try:
            return GetId().execute(book_id)
        except RuntimeError as exec:
            return errors[exec.err_type]
        except Exception as exec:
            return errors['ERROR_SERVER']
    
    @staticmethod
    def update(book_id:UUID,book:BookPath):
        try:
            return Update().execute(book_id,book)
        except RuntimeError as exec:
            return errors[exec.err_type]
        except Exception as exec:
            return errors['ERROR_SERVER']
    
    @staticmethod
    def delete(book_id:UUID):
        try:
            return Delete().execute(book_id)
        except RuntimeError as exec:
            return errors[exec.err_type]
        except Exception as exec:
            return errors['ERROR_SERVER']
    
        
