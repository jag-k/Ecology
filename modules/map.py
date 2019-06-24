import requests


def get_coords(city=71):
    URL = "https://recyclemap.ru/index.php?option=com_greenmarkers&task=get_json&type=points&tmpl=component"
    data = requests.post(URL, {
        "city": city,
        "layer": 0,
        "gos": 0
    })
    return data.json()


if __name__ == '__main__':
    from pprint import pprint
    pprint(get_coords())
