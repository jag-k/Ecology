import json
from random import randrange

from tinydb import TinyDB, Query
from tinydb.database import Table, Element

db = TinyDB("data_base.json")
user_data = db.table("user_data")  # type: Table
quest = db.table("quest")  # type: Table

User = Query()
QUESTS_DATA = json.load(open('quests.json'))

VK_ID = "vk_id"
BATTERY = "battery"
PLASTIC = "plastic"
LAMPS = "lamps"
XP = "xp"
QUESTS = "quests"


""" Format (user_data table):
|  vk_id  |  battery  |  plastic  |  lamps  |  xp  |  quests  |
Format (quests column)
[
  {
     description,
     completed
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
            XP: 0,
            QUESTS: []
        })
    return user_data.search(User.vk_id == user_id)[0]


def get_user(user_id) -> Element:
    return user_data.search(User.vk_id == user_id)[0]


def get_random_quest(user_id, count=1):
    quests = []
    for i in range(count):
        quest = QUESTS_DATA[randrange(0, len(QUESTS_DATA))]
        quests.append(quest)
        q = get_user(user_id).get(QUESTS).append(quest)
        user_data.update({QUESTS: q}, User.vk_id == user_id)
    return quests

