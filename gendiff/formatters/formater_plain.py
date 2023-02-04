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


ADDED = 'added'
REMOVED = 'removed'
UNCHANGED = 'unchanged'
UPDATED = 'updated'
NESTED = 'nested'
INNER_UPDATED = 'inner_updated'


def formatter_plain(diffdict: dict, key1=None) -> str:
    result = ''
    for key in diffdict:
        if diffdict[key]['type'] == UNCHANGED:
            continue
        if key1:
            result += f"Property {key1}."
        else:
            result += f"{key}"
        if diffdict[key]['type'] == ADDED:
            result += f" was added with value: {diffdict[key]['value']}\n"
        elif diffdict[key]['type'] == REMOVED:
            result += f" was removed\n"
        elif diffdict[key]['type'] == UPDATED:
            result += f" was updated. From {diffdict[key]['old_value']} to {diffdict[key]['new_value']}\n"
        elif diffdict[key]['type'] == INNER_UPDATED:
            if diffdict[key]['value'] and isinstance(diffdict[key]['value'], dict):
                result += f"{formatter_plain(diffdict[key]['value'], key1=key)}"
    return result


print(formatter_plain(dictt))