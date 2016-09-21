from bottle import Bottle, response

"""
    Micro Bottle.py OOP REST library
    ---
    Author: Jack Stdin <hellotan@live.ru>
"""

HTTP_METHODS = ["get", "post", "put", "patch", "options", "delete"]


class Route(object):
    def __init__(self, route):
        self.route_path = route

    def __call__(self, obj):
        allowed_methods = set()
        allowed_methods.add('OPTIONS', )

        for meth_name, meth_pointer in obj.__dict__.items():
            if meth_name.lower() in HTTP_METHODS:
                route_callback = lambda mp=meth_pointer, *args, **kwargs: mp(obj, *args, **kwargs)
                app.route(self.route_path, method=meth_name.upper())(route_callback)
                allowed_methods.add(meth_name.upper())

        app.route(self.route_path, method='OPTIONS', callback=lambda *args, **kwargs: (
            response.add_header("Access-Control-Allow-Methods", ', '.join(allowed_methods)),
            response.add_header("Access-Control-Allow-Origin", "*"),
            response.add_header("Access-Control-Allow-Headers",
                                "x-requested-with, content-type, accept, origin, authorization, x-csrftoken, user-agent, accept-encoding")
        ))
        return obj


class Error(object):
    def __init__(self, error_codes):
        if isinstance(error_codes, list):
            self.error_codes = error_codes
        else:
            self.error_codes = [error_codes]

    def __call__(self, obj):
        for error_code in self.error_codes:
            app.error_handler[error_code] = obj


app = Bottle()
