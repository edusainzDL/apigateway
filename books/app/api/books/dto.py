from app.core.success import responses as success

class BookDTO:
    
    def response(self, data, msg_key):
        return {
           "message":success[msg_key],
           "data"   : self.__format_data(data)
        }
    
    def response_all(self, data, msg_key):
        return {
           "message": success[msg_key],
           "data"   : list(map(self.__format_data,data))
        }

    def __format_data(self, data):
        return {
            "id" : data.id,
            "name" : data.name,
            "author" : data.author,
            "ean" : data.ean,
            "price" : data.price,
        }