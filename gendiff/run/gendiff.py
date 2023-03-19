from .parser import parser
from gendiff.formatters.all_formatters import format_change


ADDED = 'added'
REMOVED = 'removed'
UNCHANGED = 'unchanged'
UPDATED = 'updated'
NESTED = 'nested'
INNER_UPDATED = 'inner_updated'


def make_diff(file1, file2):

    all_keys = list(file1.keys() | file2.keys())
    all_keys.sort()
    diff_dict = {}

    for key in all_keys:

        if key in file1.keys() and key in file2.keys():
            if file1[key] != file2[key]:
                if isinstance(file1[key], dict)\
                        and isinstance(file2[key], dict):
                    diff_dict[key] = {'type': INNER_UPDATED,
                                      'value': make_diff(file1[key],
                                                         file2[key])}

                else:
                    diff_dict[key] = {'type': UPDATED,
                                      'old_value': file1[key],
                                      'new_value': file2[key]}

            else:
                diff_dict[key] = {'type': UNCHANGED,
                                  'value': file1[key]}

        elif key in file1:
            diff_dict[key] = {'type': REMOVED,
                              'value': file1[key]}

        elif key in file2:
            diff_dict[key] = {'type': ADDED,
                              'value': file2[key]}

    return diff_dict


def generate_diff(file1, file2, format_name='stylish'):
    f1 = parser(file1)
    f2 = parser(file2)
    diff_dict = make_diff(f1, f2)
    return format_change(diff_dict, format_name)
