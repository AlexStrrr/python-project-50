# dictt = {'common': {'type': 'inner_updated',
#             'value': {'follow': {'type': 'added', 'value': False},
#                       'setting1': {'type': 'unchanged', 'value': 'Value 1'},
#                       'setting2': {'type': 'removed', 'value': 200},
#                       'setting3': {'new_value': None,
#                                    'old_value': True,
#                                    'type': 'updated'},
#                       'setting4': {'type': 'added', 'value': 'blah blah'},
#                       'setting5': {'type': 'added',
#                                    'value': {'key5': 'value5'}},
#                       'setting6': {'type': 'inner_updated',
#                                    'value': {'doge': {'type': 'inner_updated',
#                                                       'value': {'wow': {'new_value': 'so '
#                                                                                      'much',
#                                                                         'old_value': '',
#                                                                         'type': 'updated'}}},
#                                              'key': {'type': 'unchanged',
#                                                      'value': 'value'},
#                                              'ops': {'type': 'added',
#                                                      'value': 'vops'}}}}},
#  'group1': {'type': 'inner_updated',
#             'value': {'baz': {'new_value': 'bars',
#                               'old_value': 'bas',
#                               'type': 'updated'},
#                       'foo': {'type': 'unchanged', 'value': 'bar'},
#                       'nest': {'new_value': 'str',
#                                'old_value': {'key': 'value'},
#                                'type': 'updated'}}},
#  'group2': {'type': 'removed', 'value': {'abc': 12345, 'deep': {'id': 45}}},
#  'group3': {'type': 'added',
#             'value': {'deep': {'id': {'number': 45}}, 'fee': 100500}}}
#
# import itertools
# import json
#
# ADDED = 'added'
# REMOVED = 'removed'
# UNCHANGED = 'unchanged'
# UPDATED = 'updated'
# NESTED = 'nested'
# INNER_UPDATED = 'inner_updated'
# COMPLEX_VALUE = 'complex_value'
#
#
# ADDED_TEMPL = "Property '{}' was added with value: {}"
# REMOVED_TEMPL = "Property '{}' was removed"
# UPDATED_TEMPL = "Property '{}' was updated. From {} to {}"
# PATH = "{}.{}"
#
#
# # def recurse(diffdict, path=''):
# #     for key in diffdict:
# #         for rv in recurse(diffdict[key], path + key):
# #             return rv
# #     else:
# #         return path
#
#
#
# #print(recurse(dictt))
#
#
# # def formatter_plain(diffdict: dict, source='') -> str:
# #     result = ''
# #     for key in diffdict:
# #         path = PATH.format(source, key) if source else key
# #         if diffdict[key]['type'] == ADDED:
# #             result += f"Property {path} was added with value: {diffdict[key]['value']}\n"
# #         elif diffdict[key]['type'] == REMOVED:
# #             result += f"Property {path} was removed\n"
# #         elif diffdict[key]['type'] == UPDATED:
# #             result += f"Property {path} was updated. From {diffdict[key]['old_value']}" \
# #                       f" to {diffdict[key]['new_value']}\n"
# #         # elif diffdict[key]['type'] == INNER_UPDATED:
# #         #     if diffdict[key]['value'] and isinstance(diffdict[key]['value'], dict):
# #         #         result += f"{formatter_plain(diffdict[key]['value'], source)}"
# #     return result


import itertools
import json


def get_value(val):

    if isinstance(val, dict):
        output_val = '[complex value]'
    elif isinstance(val, bool) or val is None:
        output_val = json.dumps(val)
    elif isinstance(val, int) or isinstance(val, float):
        output_val = str(val)
    elif isinstance(val, str):
        output_val = f"'{str(val)}'"
    return output_val


def get_dict(diffdict):
    return dict(filter(lambda item: item[1]['type'] != 'unchanged', diffdict.items()))


def plain_formatter(diffdict):
    path = []

    def make_lines(item, path):
        name, attributes = item
        status = attributes['type']
        new_line = ''
        path_record = list(itertools.chain(path, [str(name)]))

        if status == 'internal_change':
            children = attributes['value']
            new_line += '\n'.join(list(map(
                                 lambda item: make_lines(item, path_record),
                                 get_dict(children).items())))

        elif status == 'added':
            val = attributes['value']
            new_line += "Property '{}' was added with value: {}".format(
                '.'.join(path_record), get_value(val))

        elif status == 'deleted':
            new_line += "Property '{}' was removed".format('.'.join(path_record))

        elif status == 'changed_value':
            del_val, add_val = attributes['value']
            new_line += "Property '{}' was updated. From {} to {}".format(
                '.'.join(path_record), get_value(del_val), get_value(add_val))

        return new_line

    return '\n'.join(list(map(lambda item: make_lines(item, path),
                              get_dict(diffdict).items())))
