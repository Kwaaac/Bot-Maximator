import json
from random import choice


def get_json(part=None, rule=None):
    with open("sentences.json", "r", encoding='utf-8') as jsonFile:
        if part is not None:
            if rule is not None:
                return json.loads(jsonFile.read())[part][rule]

            return json.loads(jsonFile.read())[part]
        return json.loads(jsonFile.read())


def get_random_feur():
    return choice(get_json('quoi'))

