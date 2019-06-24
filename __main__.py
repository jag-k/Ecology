import bottle
from modules import *

app = bottle.Bottle()
api = API('api')

api.add_method(GET, get_coords)

if __name__ == '__main__':
    api.connect(app)
    bottle.run(
        app,
        host='0.0.0.0',
        port=80
    )
