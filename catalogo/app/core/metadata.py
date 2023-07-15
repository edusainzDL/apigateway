class Metadata:
    __title = "Api de catalogos"
    
    __version = "V1.0"

    __tags_metadata = [
        {
            "name"          : "Catalogo",
            "description"   : "Catalogo de productos"
        }
    ]

    __description = """
    Api de catalogo para probar infraestrutura de un div y provar protocolos grahql y grhp
    """

    @property
    def title(self):
        return self.__title
    
    @property
    def version(self):
        return self.__version
    
    @property
    def description(self):
        return self.__description
    
    @property
    def tags_metadata(self):
        return self.__tags_metadata