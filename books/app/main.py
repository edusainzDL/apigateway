from app.core.metadata import Metadata
from app.core.server import Server
from app.core.router import Router
from app.core.settings import settings
from app.database.database import Database

Base = Database.Base
metadata = Metadata()

config = {
    "title"         : metadata.title,
    "version"       : metadata.version,
    "description"   : metadata.description,
    "tags_metadata" : metadata.tags_metadata
}

server = Server(config)
app = server.init()
version = settings.API_VERSION
router = Router()
routes = router.get_router()
server.add_routes(routes, version)