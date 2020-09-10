from functools import wraps
import ujson


def json(handler):
    @wraps(handler)
    def wrapper(request, response):
        response.content_type = 'application/json'
        response.response_encoding = 'utf-8'
        body = handler(request, response)
        body = ujson.dumps(body)
        body = response.encode_response(body)
        return body
    return wrapper


def html(handler):
    @wraps(handler)
    def wrapper(request, response):
        response.content_type = 'text/html'
        response.response_encoding = 'utf-8'
        body = handler(request, response)
        body = response.encode_response(body)
        return body
    return wrapper