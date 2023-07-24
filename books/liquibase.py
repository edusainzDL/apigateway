from sqlalchemy.schema import CreateTable
from app.api.books.model import Book
from app.database.database import Database

db = Database()
__database = list(db.keys())[0]
print(__database)
with db[__database].engine.begin() as conn:

    ddl_commands = []
    for table in db[__database].Base.metadata.sorted_tables:
        ddl_commands.append(str(CreateTable(table).compile(conn)))
    
    with open('migrations/liquibase_changelog.sql','w') as sql_file:
        sql_file.write('\n\n'.join(ddl_commands))

