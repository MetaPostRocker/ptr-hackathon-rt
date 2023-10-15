from rest_framework import status
from rest_framework.exceptions import APIException


class MethodRequiresFilterException(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = 'List method requires filtering by field(s) {filter_fields}'
    default_code = 'method_requires_filtering'

    def __init__(self, filter_field_names: list[str] | tuple[str], code=None):
        detail = self.default_detail.format(filter_fields=', '.join(f"'{item}'" for item in filter_field_names))
        super().__init__(detail, code)
