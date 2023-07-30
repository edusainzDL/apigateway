from app.api.books.domain.create import Create
from app.api.books.domain.get_all import GetAll
from app.api.books.domain.get_id import GetId
from app.api.books.domain.update import Update
from app.api.books.domain.delete import Delete
from app.core.errors import responses as errors
from app.core.request_response import request_error
from app.api.books.schema import (
    BookCreate,
    BookPath,
    BookResponse,
    BookResponseAll
)
from uuid import UUID
import traceback
class Controller:
    @staticmethod
    def create(book:BookCreate):
        try:
            return Create().execute(book)
        except Exception as exec:
            traceback.print_exc()
            return request_error(exec)
        
    @staticmethod
    def get_all():
        try:
            return GetAll().execute()
        except Exception as exec:
            traceback.print_exc()
            return request_error(exec)
    @staticmethod
    def get_id(book_id:UUID):
        try:
            return GetId().execute(book_id)
        except Exception as exec:
            traceback.print_exc()
            return request_error(exec)
    
    @staticmethod
    def update(book_id:UUID,book:BookPath):
        try:
            return Update().execute(book_id,book)
        except Exception as exec:
            traceback.print_exc()
            return request_error(exec)
    
    @staticmethod
    def delete(book_id:UUID):
        try:
            return Delete().execute(book_id)
        except Exception as exec:
            traceback.print_exc()
            return request_error(exec)
    
        
