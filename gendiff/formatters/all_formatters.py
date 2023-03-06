from gendiff.formatters.json_formatter import json_format
from gendiff.formatters.stylish import stylish_format
from gendiff.formatters.plain import plain_format


STYLISH = 'stylish'
PLAIN = 'plain'
JSON = 'json'
DEFAULT_FORMAT = STYLISH
FORMATS = (STYLISH, PLAIN, JSON)


def format_change(diff_dict: dict, format_name: str):
    if format_name == STYLISH:
        return stylish_format(diff_dict)
    elif format_name == PLAIN:
        return plain_format(diff_dict)
    elif format_name == JSON:
        return json_format(diff_dict)
    else:
        raise ValueError(f"{format_name} is not supported. "
                         f"Please use {STYLISH}, {PLAIN} or {JSON} format")
