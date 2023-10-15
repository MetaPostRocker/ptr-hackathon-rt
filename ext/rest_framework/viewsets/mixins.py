from ext.rest_framework.api_exceptions import MethodRequiresFilterException


class ListRequiresFilterMixin:
    """
        Add this mixin to require filtering on list endpoint.
        Filter names (query parameters) must be specified in require_filter_by attribute.
        If request is made without specified filters, MethodRequiresFilterException is raised, DRF will render it as a proper API error.

        Usage:
        Add this mixin before ListModelMixin (or ModelViewSet)
    """
    @property
    def require_filter_by(self) -> list[str]:
        raise NotImplementedError('You must specify require_filter_by attribute')

    def list(self, request, *args, **kwargs):
        if set(self.require_filter_by) - set(request.query_params):
            raise MethodRequiresFilterException(filter_field_names=self.require_filter_by)

        return super().list(request, *args, **kwargs)
