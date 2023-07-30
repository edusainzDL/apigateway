from app.database.database import Database
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import String, Numeric
from sqlalchemy.orm import Mapped,mapped_column
from uuid import uuid4

class Book(Database.Base):

    __tablename__ = 'books'

    id : Mapped[UUID] = mapped_column(UUID(as_uuid=True),default=uuid4, primary_key=True)
    name : Mapped[str] = mapped_column(String(100))
    author : Mapped[str] = mapped_column(String(100))
    ean : Mapped[str] = mapped_column(String(15),nullable=True)
    price : Mapped[float] = mapped_column(Numeric(12,2))




