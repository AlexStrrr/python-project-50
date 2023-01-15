import json


def gen_diff_json(file1, file2):
    result = ''
    keys = list(file1.keys() | file2.keys())
    keys.sort()
    for k in keys:
        if k in file1 and k in file2:
            if file1[k] == file2[k]:
                result += f"  {k} {file1[k]}\n"
                continue
        if k in file1:
            result += f"- {k} {file1[k]}\n"
        if k in file2:
            result += f"+ {k} {file2[k]}\n"
    print(result)


def generate_diff(file1, file2):
    f1 = json.load(open(file1))
    f2 = json.load(open(file2))
    gen_diff_json(f1, f2)


generate_diff('file1.json', 'file2.json')
