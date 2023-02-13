import json

ADDED = 'added'
REMOVED = 'removed'
UNCHANGED = 'unchanged'
UPDATED = 'updated'
NESTED = 'nested'
INNER_UPDATED = 'inner_updated'


SPACE = ' '
PLUS = '+'
MINUS = '-'


def stylish_format(diff_dict: dict, level=2) -> str:

    result = '{\n'

    for key in diff_dict:

        if diff_dict[key]['type'] == ADDED:
            if diff_dict[key]['value'] and isinstance(diff_dict[key]['value'], dict):
                val = json.dumps(diff_dict[key]['value'], indent=4 + level)
                result += f"{SPACE * level}{PLUS} {key}: {val}\n".replace('"', '')
            else:
                result += f"{SPACE * level}{PLUS} {key}: {diff_dict[key]['value']}\n"

        elif diff_dict[key]['type'] == REMOVED:
            if diff_dict[key]['value'] and isinstance(diff_dict[key]['value'], dict):
                val = json.dumps(diff_dict[key]['value'], indent=4 + level)
                result += f"{SPACE * level}{MINUS} {key}: {val}\n".replace('"', '')
            else:
                result += f"{SPACE * level}{MINUS} {key}: {diff_dict[key]['value']}\n"

        elif diff_dict[key]['type'] == UPDATED:
            if diff_dict[key]['old_value'] and isinstance(diff_dict[key]['old_value'], dict):
                old_val = json.dumps(diff_dict[key]['old_value'], indent=4 + level)
                result += f"{SPACE * level}{MINUS} {key}: {old_val}\n".replace('"', '')
            else:
                result += f"{SPACE * level}{MINUS} {key}: {diff_dict[key]['old_value']}\n"

            if diff_dict[key]['new_value'] and isinstance(diff_dict[key]['new_value'], dict):
                new_val = json.dumps(diff_dict[key]['new_value'], indent=4 + level)
                result += f"{SPACE * level}{MINUS} {key}: {new_val}\n".replace('"', '')
            else:
                result += f"{SPACE * level}{PLUS} {key}: {diff_dict[key]['new_value']}\n"

        elif diff_dict[key]['type'] == INNER_UPDATED:
            if diff_dict[key]['value'] and isinstance(diff_dict[key]['value'], dict):
                result += f"{SPACE * level}{SPACE} {key}: {stylish_format(diff_dict[key]['value'], level + 4)}\n"
            else:
                result += f"{SPACE * level}{SPACE} {key}: {diff_dict[key]['value']}\n"

        elif diff_dict[key]['type'] == UNCHANGED:
            if diff_dict[key]['value'] and isinstance(diff_dict[key]['value'], dict):
                val = json.dumps(diff_dict[key]['value'], indent=4 + level)
                result += f"{SPACE * level}{SPACE} {key}: {val}\n".replace('"', '')
            else:
                result += f"{SPACE * level}{SPACE} {key}: {diff_dict[key]['value']}\n"

        elif not diff_dict[key]['type'] and isinstance(diff_dict[key], dict):
            if isinstance(diff_dict[key], dict):
                val = json.dumps(diff_dict[key], indent=4 + level)
                result += f"{SPACE * level}{key}: {val}\n".replace('"', '')
            else:
                result += f"{SPACE * level}{key}: {diff_dict[key]}\n"

    return result + '}'
