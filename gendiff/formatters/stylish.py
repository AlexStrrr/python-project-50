import json

ADDED = 'added'
REMOVED = 'removed'
UNCHANGED = 'unchanged'
UPDATED = 'updated'
NESTED = 'nested'
INNER_UPDATED = 'inner_updated'


SPACE = ' '
PLUS = '+'
MINUS = '-'


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


def stylish_format(diff_dict: dict, level=2) -> str:

    result = '{\n'

    for key in diff_dict:

        if diff_dict[key]['type'] == ADDED:
            if diff_dict[key]['value'] and isinstance(diff_dict[key]['value'], dict):
                val = json.dumps(diff_dict[key]['value'], indent=4 + level)
                result += f"{SPACE * level}{PLUS} {key}: {val}\n".replace('"', '')
            else:
                result += f"{SPACE * level}{PLUS} {key}: {diff_dict[key]['value']}\n"

        elif diff_dict[key]['type'] == REMOVED:
            if diff_dict[key]['value'] and isinstance(diff_dict[key]['value'], dict):
                val = json.dumps(diff_dict[key]['value'], indent=4 + level)
                result += f"{SPACE * level}{MINUS} {key}: {val}\n".replace('"', '')
            else:
                result += f"{SPACE * level}{MINUS} {key}: {diff_dict[key]['value']}\n"

        elif diff_dict[key]['type'] == UPDATED:
            if diff_dict[key]['old_value'] and isinstance(diff_dict[key]['old_value'], dict):
                old_val = json.dumps(diff_dict[key]['old_value'], indent=4 + level)
                result += f"{SPACE * level}{MINUS} {key}: {old_val}\n".replace('"', '')
            else:
                result += f"{SPACE * level}{MINUS} {key}: {diff_dict[key]['old_value']}\n"

            if diff_dict[key]['new_value'] and isinstance(diff_dict[key]['new_value'], dict):
                new_val = json.dumps(diff_dict[key]['new_value'], indent=4 + level)
                result += f"{SPACE * level}{MINUS} {key}: {new_val}\n".replace('"', '')
            else:
                result += f"{SPACE * level}{PLUS} {key}: {diff_dict[key]['new_value']}\n"

        elif diff_dict[key]['type'] == INNER_UPDATED:
            if diff_dict[key]['value'] and isinstance(diff_dict[key]['value'], dict):
                result += f"{SPACE * level}{SPACE} {key}: {stylish_format(diff_dict[key]['value'], level + 4)}\n"
            else:
                result += f"{SPACE * level}{SPACE} {key}: {diff_dict[key]['value']}\n"

        elif diff_dict[key]['type'] == UNCHANGED:
            if diff_dict[key]['value'] and isinstance(diff_dict[key]['value'], dict):
                val = json.dumps(diff_dict[key]['value'], indent=4 + level)
                result += f"{SPACE * level}{SPACE} {key}: {val}\n".replace('"', '')
            else:
                val = json.dumps(diff_dict[key]['value'], indent=4 + level)
                result += f"{SPACE * level}{key}: {val}\n"

        elif not diff_dict[key]['type'] and isinstance(diff_dict[key], dict):
            if isinstance(diff_dict[key], dict):
                val = json.dumps(diff_dict[key], indent=4 + level)
                result += f"{SPACE * level}{key}: {val}\n".replace('"', '')
            else:
                val = json.dumps(diff_dict[key], indent=4 + level)
                result += f"{SPACE * level}{key}: {val}\n"

    return result + '}'
