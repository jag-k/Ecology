from pprint import pprint
import bottle
from bottle import static_file, redirect, request, response
from modules import *

app = bottle.Bottle()
api = API('api')

api.add_method(GET, get_coords)


@app.route('/')
def main_page():
    pprint(request.json)
    return static_file('index.html', 'dist')


@app.route('/<file:path>')
def static(file):
    if file == 'index.html':
        return bottle.HTTPError(404)
    return static_file(file, 'dist')


if __name__ == '__main__':
    api.connect(app)
    bottle.run(
        app,
        host='0.0.0.0',
        port=80
    )
