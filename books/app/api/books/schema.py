from pydantic import BaseModel,Field
from typing import List,Optional
from uuid import UUID


class BookCreate(BaseModel):
    name : str = Field(..., description="Nombre del libro")
    author : str = Field(..., description="Nombre del autor")
    ean : Optional[str] = Field(None, description="Ean del libro")
    price : float = Field(..., description="Precio del libro")

class BookPath(BaseModel):
    price : float = Field(..., description="Precio del libro")
class Book(BaseModel):
    id : UUID = Field(...,description="UUID del libro")
    name : str = Field(..., description="Nombre del libro")
    author : str = Field(..., description="Nombre del autor")
    ean : Optional[str] = Field(..., description="Ean del libro")
    price : float = Field(..., description="Precio del libro")
    
class BookResponseAll(BaseModel):
    message : str = Field(...,description="Message of reponse")
    data : List[Book] = Field(...,description="UUID del libro")

class BookResponse(BaseModel):
    message : str = Field(...,description="Message of reponse")
    data : Book = Field(...,description="UUID del libro")