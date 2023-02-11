import json


def json_format(diffdict):
    return json.dumps(diffdict, indent=3, sort_keys=True)
