# METHOD TYPE
GET, POST, PUT, DELETE = "GET", "POST", "PUT", "DELETE"

# MAP DATA
PAPER, GLASS, PLASTIC, METAL, WEAR, OTHER, DANGER_TRASH, BATTERY, LAMPS, HOME_TECH, TETRA_PACK = range(1, 12)

# DATA BASE
MAX_QUESTS = 3
VK_ID = "vk_id"
BATTERY = "battery"
PLASTIC = "plastic"
LAMPS = "lamps"
QUESTS = "quests"
TOTAL_COMPLETE = "total_complete"
SOIL = "soil"
WATER = "water"
ATMOSPHERE = "atmosphere"

# TEXT FOR QUEST PAGE
TEXT_FOR_QUEST = {
    BATTERY: {
        "title": "батарейка.",
        "header": "Чем вредны батарейки?",
        "body": [
            {
                "header": "20 кв.м",
                "text": "земли загрязняет одна батарейка"
            },
            {
                "header": "1 батарейка",
                "text": "убивает 1 ежика, 2 дерева и несколько тыс. дождевых червей"
            },
            {
                "header": "~ 97%",
                "text": "всех батареек скапливается на мусорных полигонах"
            },
            {
                "header": "400 л",
                "text": "воды загрязняет одна батарейка"
            },
        ],
        "howto": {
            "header": "Как перерабатывать батарейки?",
            "text": "Чтобы переработать батарейки нужно отправить их в один из специальных пунктов приема."
        }
    },
    PLASTIC: {
        "title": "пластик.",
        "header": "Чем вреден пластик?",
        "body": [
            {
                "header": "5%",
                "text": "пластика идет на переработку"
            },
            {
                "header": "80%",
                "text": "мусора в Мировом океане – это не переработанный пластик"
            },
            {
                "header": "100 000",
                "text": "морских живых существ ежегодно погибает от пластика"
            },
            {
                "header": "~ 10%",
                "text": "пляжного покрытия – это пластик"
            },
        ],
        "howto": {
            "header": "Как перерабатывать пластик?",
            "text": "Чтобы переработать пластик нужноотнести его в один из специальных пунктов приема."
        }
    },
    LAMPS: {
        "title": "лампочка.",
        "header": "Чем вредны лампочки?",
        "body": [
            {
                "header": "5 мг",
                "text": "ртути содержится в одной люминесцентной лампочке"
            },
            {
                "header": "1 лампочка",
                "text": "содержит ртути больше чем обыкновенный термометр"
            },
            {
                "header": "50 м³",
                "text": "ядовитых паров ртути выбрасывает одна лампочка"
            },
            {
                "header": "94%",
                "text": "лампочек выбрасывается вместе с бытовым мусором"
            },
        ],
        "howto": {
            "header": "Как перерабатывать лампочки?",
            "text": "Лампочки следует сдать в пункт приема, сгруппировать на ртутные, светодиодные и лампы накаливания."
        }
    }
}

# TEXT FOR PLANET PAGE
TEXT_FOR_PLANET = {
    SOIL: {
        "header": "почва.",
        "problem": "Батарейки портят почву, из-за чего гибнет флора. Одна батарейка загрязняет 20 квадратных метров "
                   "земли.",
        "solution": "Чтобы переработать батарейки нужно отправить их в один из специальных пунктов приема."
    },
    WATER: {
        "header": "вода.",
        "problem": "В лампочках содержится ртуть, она проникает в грунтовые воды, где происходит заражение всех "
                   "обитателей планеты.",
        "solution": "Использованные лампочки следует сдать в пункт приема."
    },
    ATMOSPHERE: {
        "header": "атмосфера.",
        "problem": "При сожжении пластика в атмосферу выбрасывается огромное количество ядовитого дыма.",
        "solution": "При переработке пластика вредные вещества в атмосферу не попадают."
    }
}
