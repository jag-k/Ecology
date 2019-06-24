import os
from typing import Dict
from modules.const import *
import bottle

function = type(lambda x: x)


class API:
    def __init__(self, path='/'):
        self.path = path
        self.methods = {}  # type: Dict[str, Dict[str, function]]

    def add_method(self, method=GET, func: function = None):
        def decorate(func: function):
            if func.__name__ not in self.methods:
                self.methods[func.__name__] = {method: func}
            else:
                self.methods[func.__name__][method] = func
            return func

        return decorate(func) if func else decorate

    def connect(self, app: bottle.Bottle):
        for name, val in self.methods.items():
            for method, func in val.items():
                path = '/' + os.path.join(self.path, name).lstrip('/')
                app.route(path, method, func, name)
                print(f'Function "{name}" connected in path "{path}" with method {method.upper()}')


if __name__ == '__main__':
    app = bottle.Bottle()
    api = API('api')

    @api.add_method()
    def some_method():
        print("hello)")

    api.connect(app)
    bottle.run(app, host='0.0.0.0', port=80)
