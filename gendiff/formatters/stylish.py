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


SPACES = '  '
PLUS = '+'
MINUS = '-'


def stylishformatter(diffdict: dict) -> str:

    result = '{\n'

    for key in diffdict:

        if diffdict[key]['type'] == ADDED:
            if diffdict[key]['value'] and isinstance(diffdict[key]['value'], dict):
                result += f"{SPACES}{PLUS} {key}:\n{SPACES}{diffdict[key]['value']}\n"
            else:
                result += f"{SPACES}{PLUS} {key}: {diffdict[key]['value']}\n"

        elif diffdict[key]['type'] == REMOVED:
            result += f"{SPACES}{MINUS} {key}: {diffdict[key]['value']}\n"

        elif diffdict[key]['type'] == UPDATED:
            result += f"{SPACES}{MINUS} {key}: {diffdict[key]['old_value']}\n"\
                      f"{SPACES}{PLUS} {key}: {diffdict[key]['new_value']}\n"

        elif diffdict[key]['type'] == INNER_UPDATED:
            if diffdict[key]['value'] and isinstance(diffdict[key]['value'], dict):
                result += f"{SPACES * 2} {key}: {stylishformatter(diffdict[key]['value'])}\n"

        else:
            result += f"{SPACES * 2}{key}: {diffdict[key]['value']}\n"

    return result + '}'


print(stylishformatter(dictt))
