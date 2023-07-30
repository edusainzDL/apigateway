
from app.core.errors import responses as errors
def request_error(err):
    if type(err.args) == tuple:
        errors[err.args[0]]
    return errors['ERROR_SERVER']