from app.api.books.dto import BookDTO
from app.api.books.dao import BookDAO
class GetAll:
    def execute(self):
        try:
            books = BookDAO().get_all()
            return BookDTO().response_all(books,"GET_ALL")
        except RuntimeError as exec:
            raise exec
        except Exception as exec:
            raise RuntimeError("ERROR_SERVER")