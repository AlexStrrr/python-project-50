import json
from yaml import safe_load


def file_reader(file):
    with open(file) as f:
        data = f.read()
    if file.endswith('.yaml') or file.endswith('.yml'):
        data_format = 'yaml'
    elif file.endswith('json'):
        data_format = 'json'
    else:
        raise ValueError('File format is not supported. '
                         'Please use YAML, YML or JSON format')
    return data, data_format


def parser(data, data_format):
    if data_format == 'yaml':
        f = safe_load(data)
    elif data_format == 'json':
        f = json.loads(data)
    return f
