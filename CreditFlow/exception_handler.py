import traceback
import pydantic
from rest_framework.exceptions import ValidationError
from rest_framework.views import exception_handler
from rest_framework.exceptions import APIException

def custom_exception_handler(exc, context):
    """Custom exception handler for RDF views to handle cases like conversion of
    pydantic validation errors and so on."""

    # Convert pydantic validation errors to RDF validation errors
    if isinstance(exc, pydantic.ValidationError):
        error_dict = {}
        for err in exc.errors():
            # First lookup the elements in the path
            error_key = error_dict
            for part in err["loc"][:-1]:
                error_key_part = error_key.get(part, {})
                if not error_key_part or not isinstance(error_key_part, dict):
                    error_key[part] = {}
                error_key = error_key[part]

            # Set the error message on the final key in the path
            error_key[err["loc"][-1]] = [err["msg"]]
        exc = ValidationError(detail=error_dict).with_traceback(exc.__traceback__)

    # Call the base exception handler and return the response
    response = exception_handler(exc, context)

    return response