
class Handler:
    
    @staticmethod
    def error_handler(content):
        return {
            "message" : content,
            "data"    : None
        }