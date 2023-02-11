from gendiff.run.gendiff import ADDED, REMOVED, UNCHANGED, UPDATED, INNER_UPDATED


def get_val(value):
    if isinstance(value, dict):
        return "[complex value]"
    elif isinstance(value, bool):
        return str.lower(str(value))
    elif value is None:
        return 'null'
    return "'" + str(value) + "'"


def plain_format(diff_dict: dict, path=[]) -> str:
    result = ''
    for key in diff_dict:
        path.append(key)
        if diff_dict[key]['type'] == UNCHANGED:
            path.pop()
            continue
        elif diff_dict[key]['type'] == ADDED:
            value = get_val(diff_dict[key]['value'])
            result += f"Property '{'.'.join(path)}' was added with value: {value}\n"
        elif diff_dict[key]['type'] == REMOVED:
            result += f"Property '{'.'.join(path)}' was removed\n"
        elif diff_dict[key]['type'] == UPDATED:
            old_value = get_val(diff_dict[key]['old_value'])
            new_value = get_val(diff_dict[key]['new_value'])
            result += f"Property '{'.'.join(path)}' was updated. From {old_value}" \
                      f" to {new_value}\n"
        elif diff_dict[key]['type'] == INNER_UPDATED:
            if diff_dict[key]['value'] and isinstance(diff_dict[key]['value'], dict):
                result += f"{plain_format(diff_dict[key]['value'], path)}"
        path.pop()
    return result
