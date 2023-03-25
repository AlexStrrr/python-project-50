from tests.fixtures.types import ADDED, REMOVED,\
    UNCHANGED, UPDATED, INNER_UPDATED, SPACE, PLUS, MINUS


def bool_null(value, stylish=True):

    if isinstance(value, bool):
        return str.lower(str(value))

    elif value is None:
        return 'null'

    elif isinstance(value, dict) and stylish is True:
        bool_null(value)

    return value


def get_stylish(key, type, value, level):

    ddict = {'removed': '-',
             'added': '+',
             'unchanged': ' '
             }

    if type in ddict:

        if isinstance(value, dict):
            val = stylish_format(value, level + 4)

        else:
            val = value

        return f"{SPACE * level}{ddict[type]} {key}: "\
               f"{bool_null(val)}\n".replace('"', '')


def stylish_format(diff_dict: dict, level=2) -> str:

    result = '{\n'

    for key in diff_dict:

        if not isinstance(diff_dict[key], dict):
            result += f"{SPACE * level}{SPACE} {key}: "\
                      f"{bool_null(diff_dict[key])}\n"

        elif diff_dict[key].get('type') == ADDED\
                or diff_dict[key].get('type') == REMOVED\
                or diff_dict[key].get('type') == UNCHANGED:
            result += get_stylish(key, diff_dict[key]['type'],
                                  diff_dict[key]['value'], level)

        elif diff_dict[key].get('type') == UPDATED:

            if diff_dict[key]['old_value']\
                    and isinstance(diff_dict[key]['old_value'], dict):
                old_val = stylish_format(diff_dict[key]['old_value'], level + 4)
                result += f"{SPACE * level}{MINUS} {key}: "\
                          f"{bool_null(old_val)}\n".replace('"', '')
            else:
                result += f"{SPACE * level}{MINUS} {key}: " \
                          f"{bool_null(diff_dict[key]['old_value'])}\n"

            if diff_dict[key]['new_value']\
                    and isinstance(diff_dict[key]['new_value'], dict):
                new_val = stylish_format(diff_dict[key]['new_value'], level + 4)
                result += f"{SPACE * level}{PLUS} {key}: "\
                          f"{bool_null(new_val)}\n".replace('"', '')
            else:
                result += f"{SPACE * level}{PLUS} {key}: "\
                          f"{bool_null(diff_dict[key]['new_value'])}\n"

        elif diff_dict[key].get('type') == INNER_UPDATED:

            if diff_dict[key]['value'] \
                    and isinstance(diff_dict[key]['value'], dict):
                result += f"{SPACE * level}{SPACE} {key}: "\
                          f"{stylish_format(diff_dict[key]['value'], level + 4)}\n"
            else:
                result += f"{SPACE * level}{SPACE} {key}: "\
                          f"{bool_null(diff_dict[key]['value'])}\n"

        else:
            result += f"{SPACE * level}{SPACE} {key}: "\
                      f"{stylish_format(diff_dict[key], level + 4)}\n".replace('"', '')

    return result + ((level - 2) * ' ') + '}'
