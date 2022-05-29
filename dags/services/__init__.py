import json


def load_config():
    f = open('conf/config.json', "r")
    config = json.load(f)
    return config


CONFIG = load_config()
