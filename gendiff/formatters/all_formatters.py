from stylish import stylish_format
from plain import plain_format
from json import json_format


STYLISH = 'stylish'
PLAIN = 'plain'
JSON = 'json'


def format_change(format_name):
    if format_name == STYLISH:
        return stylish_format(diffdict)
    elif format_name == PLAIN:
        return plain_format(diffdict)
    elif format_name == JSON:
        return json_format(diffdict)
    else:
        raise ValueError(f"{format_name} is not supported. Please use {STYLISH}, {PLAIN} or {JSON} format")