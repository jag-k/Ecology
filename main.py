from pprint import pprint

import bottle
from bottle import static_file, request, response

from db import *
from modules import *

app = bottle.Bottle()
api = API('api')

api.add_method(GET, get_coords)


@app.route('/')
def main_page():
    print("Cookie:", request.get_cookie('test'))
    response.set_cookie('test', 'name')
    p = request.params
    pprint(dict(p))
    if p.get('vk_user_id'):
        create_new_user(p.get('vk_user_id'))

    return static_file('index.html', 'dist')


@api.add_method(GET)
def get_page():
    page_name = request.params.get('page_name').lstrip('/')
    if not page_name:
        return bottle.template('dist/index.html').split('<div id="content">')[1].rsplit('</div>', 1)[0].strip()
    return bottle.template('dist/' + page_name+'.html')


api.connect(app)


@app.route('/<file:path>')
def static(file: str):
    if file.endswith('.html'):
        return bottle.HTTPError(404)
    return static_file(file, 'dist')


if __name__ == '__main__':
    bottle.run(
        app,
        host='0.0.0.0',
        port=80,
        reloader=True,
    )
