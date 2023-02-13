ADDED = 'added'
REMOVED = 'removed'
UNCHANGED = 'unchanged'
UPDATED = 'updated'
NESTED = 'nested'
INNER_UPDATED = 'inner_updated'


SPACE = ' '
TWOSPACES = '  '
PLUS = '+'
MINUS = '-'


def stylish_format(diff_dict: dict, level=2) -> str:

    result = '{\n'

    for key in diff_dict:

        if not isinstance(diff_dict[key], dict):
            result += f"{SPACE * level}{SPACE} {key}: {diff_dict[key]}\n"

        elif diff_dict[key].get('type', 0) == ADDED:
            if diff_dict[key]['value'] and isinstance(diff_dict[key]['value'], dict):
                val = stylish_format(diff_dict[key]['value'], level + 4)
                result += f"{SPACE * level}{PLUS} {key}: {val}\n".replace('"', '')
            else:
                result += f"{SPACE * level}{PLUS} {key}: {diff_dict[key]['value']}\n"

        elif diff_dict[key].get('type', 0) == REMOVED:
            if diff_dict[key]['value'] and isinstance(diff_dict[key]['value'], dict):
                val = stylish_format(diff_dict[key]['value'], level + 4)
                result += f"{SPACE * level}{MINUS} {key}: {val}\n".replace('"', '')
            else:
                result += f"{SPACE * level}{MINUS} {key}: {diff_dict[key]['value']}\n"

        elif diff_dict[key].get('type', 0) == UPDATED:
            if diff_dict[key]['old_value'] and isinstance(diff_dict[key]['old_value'], dict):
                old_val = stylish_format(diff_dict[key]['old_value'], level + 4)
                result += f"{SPACE * level}{MINUS} {key}: {old_val}\n".replace('"', '')
            else:
                result += f"{SPACE * level}{MINUS} {key}: {diff_dict[key]['old_value']}\n"

            if diff_dict[key]['new_value'] and isinstance(diff_dict[key]['new_value'], dict):
                new_val = stylish_format(diff_dict[key]['new_value'], level + 4)
                result += f"{SPACE * level}{MINUS} {key}: {new_val}\n".replace('"', '')
            else:
                result += f"{SPACE * level}{PLUS} {key}: {diff_dict[key]['new_value']}\n"

        elif diff_dict[key].get('type', 0) == INNER_UPDATED:
            if diff_dict[key]['value'] and isinstance(diff_dict[key]['value'], dict):
                result += f"{SPACE * level}{SPACE} {key}: {stylish_format(diff_dict[key]['value'], level + 4)}\n"
            else:
                result += f"{SPACE * level}{SPACE} {key}: {diff_dict[key]['value']}\n"

        elif diff_dict[key].get('type', 0) == UNCHANGED:
            if diff_dict[key]['value'] and isinstance(diff_dict[key]['value'], dict):
                val = stylish_format(diff_dict[key]['value'], level + 4)
                result += f"{SPACE * level}{SPACE} {key}: {val}\n".replace('"', '')
            else:
                result += f"{SPACE * level}{SPACE} {key}: {diff_dict[key]['value']}\n".replace('"', '')

        else:
            result += f"{SPACE * level}{SPACE} {key}: {stylish_format(diff_dict[key], level + 4)}\n".replace('"', '')

    return result + ((level - 2) * ' ') + '}'
