
from app.api.books.model import Book
from app.database.database import Database
from sqlalchemy import select

class BookDAO:

    def __init__(self) -> None:
         self.__db = Database().get_db_session()
    
    def get_all(self):
        try:
            books = self.__db.scalars(select(Book))
            return books
        except Exception as err:
            self.__db.rollback()
            raise RuntimeError('ERROR_GET_ALL')
    
    def get_id(self,book_id):
        try:
            book = self.__db.scalar(select(Book).where(Book.id == book_id))
            return book
        except Exception as err:
            self.__db.rollback()
            raise RuntimeError('ERROR_SERVER')
    
    def delete(self,book):
        try:
            self.__db.delete(book)
            self.__db.commit()
            return book
        except Exception as err:
            self.__db.rollback()
            raise RuntimeError('ERROR_DELETED')
    
    def create(self,book_schema):
        try:
            book = Book(
                name = book_schema.name,
                author = book_schema.author,
                ean = book_schema.ean,
                price = book_schema.price,


            )
            self.__db.add(book)
            self.__db.flush()

            self.__db.commit()
            self.__db.refresh(book)

            return book
        except Exception as err:
            self.__db.rollback()
            raise RuntimeError('ERROR_CREATED')
    
    def update(self,book_schema, book_db):
        try:
            book_db.price = book_schema.price
            self.__db.add(book_db)
            self.__db.flush()

            self.__db.commit()
            self.__db.refresh(book_db)

            return book_db
        except Exception as err:
            self.__db.rollback()
            raise RuntimeError('ERROR_UPDATED')

        