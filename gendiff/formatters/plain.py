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


import itertools


ADDED = 'added'
REMOVED = 'removed'
UNCHANGED = 'unchanged'
UPDATED = 'updated'
NESTED = 'nested'
INNER_UPDATED = 'inner_updated'
COMPLEX_VALUE = 'complex_value'


def get_val(value):
    if isinstance(value, dict):
        return "[complex value]"
    elif isinstance(value, bool):
        return str.lower(str(value))
    elif value is None:
        return 'null'
    return "'" + str(value) + "'"


def plain_format(diffdict: dict, source='') -> str:
    result = ''
    path = []
    for key in diffdict:
        # path = itertools.chain(path, str(key))
        # path = list(path)
        # path = ''.join(path)
        path.append(key)
        if diffdict[key]['type'] == UNCHANGED:
            continue
        elif diffdict[key]['type'] == ADDED:
            value = get_val(diffdict[key]['value'])
            result += f"Property '{path}' was added with value: {value}\n"
        elif diffdict[key]['type'] == REMOVED:
            result += f"Property '{path}' was removed\n"
        elif diffdict[key]['type'] == UPDATED:
            old_value = get_val(diffdict[key]['old_value'])
            new_value = get_val(diffdict[key]['new_value'])
            result += f"Property '{path}' was updated. From {old_value}" \
                      f" to {new_value}\n"
        elif diffdict[key]['type'] == INNER_UPDATED:
            if diffdict[key]['value'] and isinstance(diffdict[key]['value'], dict):
                path.append(key)
                result += f"{plain_format(diffdict[key]['value'], source)}"
    return result


print(plain_format(dictt))

