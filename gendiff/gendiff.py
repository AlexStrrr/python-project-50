from gendiff.parser import parser
from gendiff.formatters.all_formatters import format_change


ADDED = 'added'
REMOVED = 'removed'
UNCHANGED = 'unchanged'
UPDATED = 'updated'
NESTED = 'nested'
INNER_UPDATED = 'inner_updated'


def make_diff(f1, f2):

    all_keys = list(f1.keys() | f2.keys())
    all_keys.sort()
    diff_dict = {}

    for key in all_keys:

        if key in f1 and key not in f2:
            diff_dict[key] = {'type': REMOVED,
                              'value': f1[key]}

        elif key in f2 and key not in f1:
            diff_dict[key] = {'type': ADDED,
                              'value': f2[key]}

        elif f1[key] == f2[key]:
                diff_dict[key] = {'type': UNCHANGED,
                                  'value': f1[key]}

        elif isinstance(f1[key], dict)\
                    and isinstance(f2[key], dict):
                diff_dict[key] = {'type': INNER_UPDATED,
                                  'value': make_diff(f1[key],
                                                     f2[key])}

        else:
            diff_dict[key] = {'type': UPDATED,
                              'old_value': f1[key],
                              'new_value': f2[key]}

    return diff_dict


# def make_diff(f1, f2):
# 
#     all_keys = list(f1.keys() | f2.keys())
#     all_keys.sort()
#     diff_dict = {}
# 
#     for key in all_keys:
# 
#         if key in f1.keys() and key in f2.keys():
#             if f1[key] != f2[key]:
#                 if isinstance(f1[key], dict)\
#                         and isinstance(f2[key], dict):
#                     diff_dict[key] = {'type': INNER_UPDATED,
#                                       'value': make_diff(f1[key],
#                                                          f2[key])}
# 
#                 else:
#                     diff_dict[key] = {'type': UPDATED,
#                                       'old_value': f1[key],
#                                       'new_value': f2[key]}
# 
#             else:
#                 diff_dict[key] = {'type': UNCHANGED,
#                                   'value': f1[key]}
# 
#         elif key in f1:
#             diff_dict[key] = {'type': REMOVED,
#                               'value': f1[key]}
# 
#         elif key in f2:
#             diff_dict[key] = {'type': ADDED,
#                               'value': f2[key]}
# 
#     return diff_dict


def generate_diff(file1, file2, format_name='stylish'):
    f1 = parser(file1)
    f2 = parser(file2)
    diff_dict = make_diff(f1, f2)
    return format_change(diff_dict, format_name)
