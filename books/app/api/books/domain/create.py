
from app.api.books.dto import BookDTO
from app.api.books.dao import BookDAO

class Create:
    
    def execute(self, book):
        try:
            book = BookDAO().create(book)
            return BookDTO().response(book,"CREATED")
        except RuntimeError as exec:
            raise exec
        except Exception as exec:
            raise RuntimeError("ERROR_SERVER")