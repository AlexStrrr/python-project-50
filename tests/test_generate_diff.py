import json

from gendiff.gendiff import generate_diff
from gendiff.gendiff import make_diff
from gendiff.formatters.stylish import stylishformatter


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


def test_formatter_stylish():
    with open("tests/fixtures/file3.json") as file3:
        dict3 = json.load(file3)
    with open("tests/fixtures/file4.json") as file4:
        dict4 = json.load(file4)
    dict = make_diff(dict3, dict4)
    result = stylishformatter(dict)
    assert result == open("tests/fixtures/results/stylish.txt").read()
