import json


def json_format(diff_dict: dict):
    return json.dumps(diff_dict, indent=3, sort_keys=True)
