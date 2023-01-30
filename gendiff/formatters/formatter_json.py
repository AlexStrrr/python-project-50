dictt = {'common': {'type': 'internal_change',
            'value': {'follow': {'type': 'added', 'value': False},
                      'setting1': {'type': 'unchanged', 'value': 'Value 1'},
                      'setting2': {'type': 'deleted', 'value': 200},
                      'setting3': {'new_value': None,
                                   'old_value': True,
                                   'type': 'changed'},
                      'setting4': {'type': 'added', 'value': 'blah blah'},
                      'setting5': {'type': 'added',
                                   'value': {'key5': 'value5'}},
                      'setting6': {'type': 'internal_change',
                                   'value': {'doge': {'type': 'internal_change',
                                                      'value': {'wow': {'new_value': 'so '
                                                                                     'much',
                                                                        'old_value': '',
                                                                        'type': 'changed'}}},
                                             'key': {'type': 'unchanged',
                                                     'value': 'value'},
                                             'ops': {'type': 'added',
                                                     'value': 'vops'}}}}},
 'group1': {'type': 'internal_change',
            'value': {'baz': {'new_value': 'bars',
                              'old_value': 'bas',
                              'type': 'changed'},
                      'foo': {'type': 'unchanged', 'value': 'bar'},
                      'nest': {'new_value': 'str',
                               'old_value': {'key': 'value'},
                               'type': 'changed'}}},
 'group2': {'type': 'deleted', 'value': {'abc': 12345, 'deep': {'id': 45}}},
 'group3': {'type': 'added',
            'value': {'deep': {'id': {'number': 45}}, 'fee': 100500}}}


# FORMATS = {'json': {'added': '+',
#                     'deleted': '-',
#                     'changed': ''}


def formater_json(dict1: dict) -> str:
    result = '{\n'
    for key in dict1:
        if 'value' in dict1[key].keys() and isinstance(dict1[key]['value'], dict):
            result += formater_json(dict1[key]['value'])
        else:
            if dict1[key]['type'] == 'added':
                result += f"    + {key}: {dict1[key]['value']}\n"
            elif dict1[key]['type'] == 'deleted':
                result += f"    - {key}: {dict1[key]['value']}\n"
            elif dict1[key]['type'] == 'changed':
                result += f"    - {key}: {dict1[key]['old_value']}\n"\
                          f"    + {key}: {dict1[key]['new_value']}\n"
            else:
                result += f"      {key}: {dict1[key]['value']}\n"
    print(result + '}')
    return result + '}'


formater_json(dictt)