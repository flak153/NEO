import requests
import json

url = "http://neocrisis.xyz/telescope/"


def get_positions():
    objects = []
    for x in range(1, 9):
        response = requests.get(url+str(x))
        loaded = json.loads(response.text)
        for obj in loaded['objects']:
            if obj["type"] == "rock":
                objects.append(tuple((obj["name"], obj["obs_time"], obj["pos"])))
    return objects


def get_zipped():
    first = sorted(get_positions())
    second = sorted(get_positions())

    print(first)
    print(second)
    zipped = zip(first, second)

    #print(json.dumps(list(zipped), indent= 2))

    return zipped
