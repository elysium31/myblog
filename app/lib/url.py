from flask import request, url_for


def url_current(**kwargs):
    if not request.endpoint:
        return None
    url_kwargs = (request.view_args or {}).copy()
    url_kwargs.update(kwargs)
    return url_for(request.endpoint, **url_kwargs)