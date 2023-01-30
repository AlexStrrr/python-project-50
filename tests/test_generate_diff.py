import json

from gendiff.gendiff import generate_diff
from gendiff.gendiff import make_diff


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
    assert result == {'follow': {'type': 'deleted', 'value': False},
 'host': {'type': 'unchanged', 'value': 'hexlet.io'},
 'proxy': {'type': 'deleted', 'value': '123.234.53.22'},
 'timeout': {'new_value': 20, 'old_value': 50, 'type': 'changed'},
 'verbose': {'type': 'added', 'value': True}}
