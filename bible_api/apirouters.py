# FROM: https://www.django-rest-framework.org/api-guide/routers/#defaultrouter
from rest_framework.routers import Route, DynamicRoute, SimpleRouter

class BCV_Lookup(SimpleRouter):
    """
    A router for read-only APIs, which doesn't use trailing slashes.
    """
    routes = [
        Route(
            #url=r'^api/{book}/{chapter}/{verse}$',
            url=r'^api/{prefix}$',
            mapping={'get': 'list'},
            name='book',
            detail=True,
            initkwargs={'suffix': 'List'}
        )
    ]