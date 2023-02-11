import json
from yaml import safe_load


def parser(filepath):
    with open(filepath) as f:
        if filepath.endswith('.yaml') or filepath.endswith('.yml'):
            f = safe_load(open(filepath))
        elif filepath.endswith('.json'):
            f = json.load(open(filepath))
    return f
