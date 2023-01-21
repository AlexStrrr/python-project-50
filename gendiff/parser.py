import json
import yaml


def parser(filepath):
    with open(filepath) as file:
        if filepath.endswith('.yaml') or filepath.endswith('.yml'):
            f = yaml.load(open(filepath))
        elif filepath.endswith('.json'):
            f = json.load(open(filepath))
    return f
