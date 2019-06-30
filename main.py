from pprint import pprint

import bottle
from bottle import static_file, request, template

from db import *
from modules import *

app = bottle.Bottle()
api = API('api')

api.add_method(GET, get_coords)


@app.route('/')
def main_page():
    p = dict(request.params)
    pprint(p)
    if p.get('vk_user_id'):
        user_id = p.get('vk_user_id')
        create_new_user(user_id)
        quests = []
        for q in get_user(user_id).get(QUESTS):
            quests.append('<a href="/quest_page.html" class="progress">%s'
                          '<div class="line"></div>'
                          '<span class="bold">%s/%s</span>'
                          '</a>' % (q['description'], q['completed'], q['needed']))

    return template('dist/index.html', quests=''.join(quests or []))


@api.add_method(GET)
def get_page():
    data = {}
    call_function = ''
    params = dict(request.params)
    page_name = params.get('page_name').lstrip('/')
    if page_name == "quest_page":  # ?user_id=123&quest_id=3
        user_id = params.get('user_id')
        quest_id = max(1, min(int(params.get('quest_id')), MAX_QUESTS)) - 1
        print(get_user(user_id).get(QUESTS))
        quest = get_user(user_id).get(QUESTS)[quest_id]
        data = TEXT_FOR_QUEST.get(quest.get('type'))
        page_name = 'quest_page'
        call_function = 'quest_init'

    if not page_name:
        return {
            "call_func": call_function,
            "data": data,
            "page": template('dist/index.html').split('<div id="content">')[1].rsplit('</div>', 1)[0].strip()
        }
    return {
        "call_func": call_function,
        "data": data,
        "page": template('dist/' + page_name+'.html')
    }


@api.add_method(GET)
def get_quest_info():  # ?user_id=123&quest_id=3
    params = dict(request.params)
    user_id = params.get('user_id')
    quest_id = max(0, min(params.get('quest_id'), MAX_QUESTS))
    return get_user(user_id).get(QUESTS)[quest_id]


@api.add_method(GET)
def add_item_in_quest():  # ?user_id=123&quest_id=3&count=1
    params = dict(request.params)
    user_id = params.get('user_id')
    count = params.get('count', 0)
    quest_id = max(0, min(params.get('quest_id'), MAX_QUESTS))
    quest = get_user(user_id).get(QUESTS)[quest_id]
    quest['needed'] = max(0, quest['needed']-count)
    update_quest(user_id, quest_id, quest)
    return quest


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
