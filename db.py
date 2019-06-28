import json
from random import randrange
from time import time

from tinydb import TinyDB, Query
from tinydb.database import Table, Element

from modules import *

db = TinyDB("data_base.json")
user_data = db.table("user_data")  # type: Table
quest = db.table("quest")  # type: Table

User = Query()
QUESTS_DATA = json.load(open('quests.json'))


""" Format (user_data table):
|  vk_id  |  battery  |  plastic  |  lamps  |  quests  |  total_complete  |
Format (quests column)
[
  {
     description,
     type [battery|plastic|lamps],
     start_time,
     completed,
     needed
  }
]
"""


def create_new_user(user_id):
    if not user_data.search(User.vk_id == user_id):
        user_data.insert({
            VK_ID: user_id,
            BATTERY: 0,
            PLASTIC: 0,
            LAMPS: 0,
            TOTAL_COMPLETE: 0,
            QUESTS: []
        })
    return user_data.search(User.vk_id == user_id)[0]


def get_user(user_id) -> Element:
    return user_data.search(User.vk_id == user_id)[0]


def generate_random_quest(user_id):
    quests = []
    start_time = time()
    quest_list = get_user(user_id).get(QUESTS)
    for i in range(MAX_QUESTS - len(quest_list)):
        quest_dat = QUESTS_DATA[randrange(0, len(QUESTS_DATA))]
        needed = quest_dat.get('needed')
        quest = {"description": quest_dat.get('description'), "type": needed['type'], "start_time": start_time,
                 "completed": 0, "needed": needed['count']}
        quests.append(quest)
        quest_list.append(quest)
    user_data.update({QUESTS: quest_list}, User.vk_id == user_id)
    return quests

