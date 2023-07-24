from app.api.books.dto import BookDTO
from app.api.books.dao import BookDAO
class Delete:
    def execute(self, book_id):
        try:
            book = BookDAO().get_id(book_id)
            if book is None:
                raise RuntimeError('ERROR_NOT_FOUND')
            book = BookDAO().delete(book_id)
            return BookDTO().response(book,"DELETED")
        except RuntimeError as exec:
            raise exec
        except Exception as exec:
            raise RuntimeError("ERROR_SERVER")