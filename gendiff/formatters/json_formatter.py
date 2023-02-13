import json


def json_format(diff_dict: dict):
    return json.dumps(diff_dict, indent=4, sort_keys=True)
