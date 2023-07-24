from app.api.books.dto import BookDTO
from app.api.books.dao import BookDAO
class Update:
    def execute(self, book_id,book_schema):
        try:
            book = BookDAO().get_id(book_id)
            if book is None:
                raise RuntimeError('ERROR_NOT_FOUND')
            book = BookDAO().update(book_schema,book)
            return BookDTO().response(book,"UPDATED")
        except RuntimeError as exec:
            raise exec
        except Exception as exec:
            raise RuntimeError("ERROR_SERVER")