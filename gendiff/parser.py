import json
from yaml import safe_load

import requests


def file_reader(file):
    with open(file) as f:
        data = f.read()
    if file.endswitch('.yaml'):
        data_format = 'yaml'
    elif file.endswitch('yml'):
        data_format = 'yml'
    elif file.endswitch('json'):
        data_format = 'json'
    else:
        raise ValueError('File format is not supported. Please use YAML, YML or JSON format')
    return data and data_format


def parser(data, data_format):
    if data_format == 'yaml' or data_format == 'yml':
        f = safe_load(data)
    elif data_format == 'json':
        f = json.load(data)
    return f


# json_data = requests.get("https://something.com/json-data").text
# parsed_data = parser(json_data, 'json')
# print(parsed_data)