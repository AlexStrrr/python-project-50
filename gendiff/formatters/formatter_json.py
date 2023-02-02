dictt = {'common': {'type': 'changed',
            'value': {'follow': {'type': 'added', 'value': False},
                      'setting1': {'type': 'unchanged', 'value': 'Value 1'},
                      'setting2': {'type': 'deleted', 'value': 200},
                      'setting3': {'new_value': None,
                                   'old_value': True,
                                   'type': 'changed'},
                      'setting4': {'type': 'added', 'value': 'blah blah'},
                      'setting5': {'type': 'added',
                                   'value': {'key5': 'value5'}},
                      'setting6': {'type': 'changed',
                                   'value': {'doge': {'type': 'changed',
                                                      'value': {'wow': {'new_value': 'so '
                                                                                     'much',
                                                                        'old_value': '',
                                                                        'type': 'changed'}}},
                                             'key': {'type': 'unchanged',
                                                     'value': 'value'},
                                             'ops': {'type': 'added',
                                                     'value': 'vops'}}}}},
 'group1': {'type': 'changed',
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


SPACES = '  '
PLUS = '+'
MINUS = '-'


def formater(diffdict: dict) -> str:
    result = '{\n'
    for key in diffdict:
        if diffdict[key]['type'] == 'added':
            result += f"{SPACES * 2}{PLUS} {key}: {diffdict[key]['value']}\n"
        elif diffdict[key]['type'] == 'deleted':
            result += f"{SPACES * 2}{MINUS} {key}: {diffdict[key]['value']}\n"
        elif diffdict[key]['type'] == 'changed':
            if diffdict[key]['value'] and isinstance(diffdict[key]['value'], dict):
                formater(diffdict[key]['value'])
            elif diffdict[key]['old_value'] and diffdict[key]['new_value']:
                result += (f"{SPACES * 2}{MINUS} {key}: {diffdict[key]['old_value']}\n"
                           f"{SPACES * 2}{MINUS} {key}: {diffdict[key]['old_value']}\n")
            else:
                result += "ВСЕ ОЧЕНЬ ПЛОХО\n"
        else:
            result += f"{SPACES * 3}{key}: {diffdict[key]['value']}\n"
    print(result + '}')
    return result + '}'


formater(dictt)
