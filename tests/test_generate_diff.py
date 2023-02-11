import json
from gendiff.run.gendiff import generate_diff
from gendiff.run.gendiff import make_diff
from gendiff.formatters.stylish import stylish_format
from gendiff.formatters.plain import plain_format


def test_gen_diff_json():
    result = generate_diff("tests/fixtures/file1.json", "tests/fixtures/file2.json")
    assert result == open("tests/fixtures/results/flat.txt").read()


def test_gen_diff_yaml():
    result = generate_diff("tests/fixtures/file1.yml", "tests/fixtures/file2.yml")
    assert result == open("tests/fixtures/results/flat.txt").read()


def test_make_diff():
    with open("tests/fixtures/file1.json") as file1:
        dict1 = json.load(file1)
    with open("tests/fixtures/file2.json") as file2:
        dict2 = json.load(file2)
    result = make_diff(dict1, dict2)
    assert result == open("tests/fixtures/results/make_diff.txt").read()


def test_stylish_format():
    with open("tests/fixtures/file3.json") as file3:
        dict3 = json.load(file3)
    with open("tests/fixtures/file4.json") as file4:
        dict4 = json.load(file4)
    diffdict = make_diff(dict3, dict4)
    result = stylish_format(diffdict)
    assert result == open("tests/fixtures/results/stylish.txt").read()


def test_plain_format():
    with open("tests/fixtures/file3.json") as file3:
        dict3 = json.load(file3)
    with open("tests/fixtures/file4.json") as file4:
        dict4 = json.load(file4)
    diff_dict = make_diff(dict3, dict4)
    result = plain_format(diff_dict)
    assert result == open("tests/fixtures/results/plain.txt").read()


def is_json(data):
    try:
        json.loads(data)
    except ValueError:
        return False
    return True


def test_json():
    result1 = generate_diff("tests/fixtures/file3.json", "tests/fixtures/file4.json", 'json')
    result2 = generate_diff("tests/fixtures/file3.json", "tests/fixtures/file4.json")
    assert is_json(result1) is True
    assert is_json(result2) is False
