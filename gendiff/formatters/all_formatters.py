from stylish import stylish_format
from plain import plain_format
from json import json_format


STYLISH = 'stylish'
PLAIN = 'plain'
JSON = 'json'


def format_change(diff_dict: dict, format_name: str):
    if format_name == STYLISH:
        return stylish_format(diff_dict)
    elif format_name == PLAIN:
        return plain_format(diff_dict)
    elif format_name == JSON:
        return json_format(diff_dict)
    else:
        raise ValueError(f"{format_name} is not supported. Please use {STYLISH}, {PLAIN} or {JSON} format")
