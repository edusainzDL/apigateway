from app.api.books.dto import BookDTO
from app.api.books.dao import BookDAO
class GetId:
    def execute(self, book_id):
        try:
            book = BookDAO().get_id(book_id)
            if book is None:
                raise RuntimeError('ERROR_NOT_FOUND')
            return BookDTO().response(book,"GET_ID")
        except RuntimeError as exec:
            raise exec
        except Exception as exec:
            raise RuntimeError("ERROR_SERVER")