import time

from fastapi import FastAPI,Request
from fastapi.responses import JSONResponse,RedirectResponse
from fastapi.exceptions import RequestValidationError
from fastapi.encoders import jsonable_encoder
from app.core.handler import Handler

class Server(FastAPI):
    
    def __init__(self, config:dict):
        self.title          = config['title']
        self.version        = config['version']
        self.description    = config['description']
        self.tags_metadata  = config['tags_metadata']

        super().__init__(
            title           = self.title,
            description     = self.description,
            version         = self.version,
            openapi_tags    = self.tags_metadata
        )
    
    def init(self):
        self.__validations()
        self.__docs_redirect()
        return self

    def add_routes(self, routes:list,version:str):
        for route in routes:
            self.include_router(route, prefix=version)

    
    def __validations(self):
        @self.exception_handler(RequestValidationError)
        async def validation_exeception_handler(request:Request, exc:RequestValidationError):
            errors      = {}
            list_error  = list()
            for error in errors:
                response = {}
                var = error['loc'][-1]
                response['var'] = var
                response['errors'] = error['msg']
                list_error.append(response)
            return JSONResponse(status_code=422, content=jsonable_encoder(Handler.error_handler(list_error)))
    
    def __docs_redirect(self):
        @self.get('/', include_in_schema=False)
        async def docs_redirect():
            return RedirectResponse(url='/docs')
        