from fastapi.responses import JSONResponse
from app.core.handler import Handler

responses = {
    "ERROR_NOT_FOUND"  : JSONResponse(status_code=400,content=Handler.error_handler("Catalogo no encontrado")),
    "ERROR_CREATED"    : JSONResponse(status_code=400,content=Handler.error_handler("Error al crear el catalogo")),
    "ERROR_UPDATED"    : JSONResponse(status_code=400,content=Handler.error_handler("Error al eliminar el catalogo")),
    "ERROR_DELETED"    : JSONResponse(status_code=400,content=Handler.error_handler("Error al eliminat el catalogo")),
    "ERROR_GET_ALL"    : JSONResponse(status_code=400,content=Handler.error_handler("Error al obtener la lista de catalogos")),
    "ERROR_SERVER"     : JSONResponse(status_code=400,content=Handler.error_handler("Error del servidor"))
}