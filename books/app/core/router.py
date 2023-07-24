from app.api.books.route import router as books_router
class Router:

    __routers = [
        books_router
    ]

    def get_router(self):
        return self.__routers
