dictt = {'common': {'type': 'inner_updated',
            'value': {'follow': {'type': 'added', 'value': False},
                      'setting1': {'type': 'unchanged', 'value': 'Value 1'},
                      'setting2': {'type': 'removed', 'value': 200},
                      'setting3': {'new_value': None,
                                   'old_value': True,
                                   'type': 'updated'},
                      'setting4': {'type': 'added', 'value': 'blah blah'},
                      'setting5': {'type': 'added',
                                   'value': {'key5': 'value5'}},
                      'setting6': {'type': 'inner_updated',
                                   'value': {'doge': {'type': 'inner_updated',
                                                      'value': {'wow': {'new_value': 'so '
                                                                                     'much',
                                                                        'old_value': '',
                                                                        'type': 'updated'}}},
                                             'key': {'type': 'unchanged',
                                                     'value': 'value'},
                                             'ops': {'type': 'added',
                                                     'value': 'vops'}}}}},
 'group1': {'type': 'inner_updated',
            'value': {'baz': {'new_value': 'bars',
                              'old_value': 'bas',
                              'type': 'updated'},
                      'foo': {'type': 'unchanged', 'value': 'bar'},
                      'nest': {'new_value': 'str',
                               'old_value': {'key': 'value'},
                               'type': 'updated'}}},
 'group2': {'type': 'removed', 'value': {'abc': 12345, 'deep': {'id': 45}}},
 'group3': {'type': 'added',
            'value': {'deep': {'id': {'number': 45}}, 'fee': 100500}}}


import json


ADDED = 'added'
REMOVED = 'removed'
UNCHANGED = 'unchanged'
UPDATED = 'updated'
NESTED = 'nested'
INNER_UPDATED = 'inner_updated'


SPACE = '  '
PLUS = '+'
MINUS = '-'


def stylish_format(diffdict: dict) -> str:

    result = '{\n'
    level = 3

    for key in diffdict:

        if diffdict[key]['type'] == ADDED:
            if diffdict[key]['value'] and isinstance(diffdict[key]['value'], dict):
                val = json.dumps(diffdict[key]['value'], indent=4)
                result += f"{SPACE * level}{PLUS} {key}'0': {val}\n".replace('"', '')
            else:
                result += f"{SPACE * level}{PLUS} {key}'1': {diffdict[key]['value']}\n"

        elif diffdict[key]['type'] == REMOVED:
            if diffdict[key]['value'] and isinstance(diffdict[key]['value'], dict):
                val = json.dumps(diffdict[key]['value'], indent=4)
                result += f"{SPACE * level}{MINUS} {key}'2': {val}\n".replace('"', '')
            else:
                result += f"{SPACE}{MINUS} {key}'3': {diffdict[key]['value']}\n"

        elif diffdict[key]['type'] == UPDATED:
            result += f"{SPACE * level}{MINUS} {key}'4': {diffdict[key]['old_value']}\n"\
                      f"{SPACE * level}{PLUS} {key}'4.5': {diffdict[key]['new_value']}\n"

        elif diffdict[key]['type'] == INNER_UPDATED:
            if diffdict[key]['value'] and isinstance(diffdict[key]['value'], dict):
                level -= 1
                result += f"{SPACE * level} {key}'5': {stylish_format(diffdict[key]['value'])}\n"
                level += 1

        elif diffdict[key]['type'] == UNCHANGED:
            if diffdict[key]['value'] and isinstance(diffdict[key]['value'], dict):
                val = json.dumps(diffdict[key]['value'], indent=4)
                result += f"{SPACE * level}{SPACE}{key}'6': {val}\n".replace('"', '')
            else:
                result += f"{SPACE * level}{SPACE}{key}'7': {diffdict[key]['value']}\n"

    return result + '}'


print(stylish_format(dictt))

