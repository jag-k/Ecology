from pprint import pprint

import bottle
from bottle import static_file, request, response

from modules import *

app = bottle.Bottle()
api = API('api')

api.add_method(GET, get_coords)


@app.route('/')
def main_page():
    print("Cookie:", request.get_cookie('test'))
    response.set_cookie('test', 'name')
    pprint(dict(request.params))
    return static_file('index.html', 'dist')


@api.add_method(GET)
def get_page():
    return static_file(request.params.get('page_name')+'.html', 'dist')


@app.route('/<file:path>')
def static(file: str):
    if file.endswith('.html'):
        return bottle.HTTPError(404)
    return static_file(file, 'dist')


if __name__ == '__main__':
    api.connect(app)
    bottle.run(
        app,
        host='0.0.0.0',
        port=80,
        reloader=True,
    )
