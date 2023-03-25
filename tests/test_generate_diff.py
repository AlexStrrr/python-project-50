import json
from gendiff.generate_diff import generate_diff
import pytest
from gendiff.formatters.all_formatters import STYLISH, PLAIN, JSON


@pytest.mark.parametrize('file1, file2, report_format, result_file',
                         [('tests/fixtures/file1.json',
                           'tests/fixtures/file2.json',
                           JSON,
                           'tests/fixtures/results/jsonflat.txt'),
                          ('tests/fixtures/file1.yaml',
                           'tests/fixtures/file2.yaml',
                           JSON,
                           'tests/fixtures/results/jsonflat.txt'),
                          ('tests/fixtures/file3.json',
                           'tests/fixtures/file4.json',
                           JSON,
                           'tests/fixtures/results/nestedjson.txt'),
                          ('tests/fixtures/file3.yaml',
                           'tests/fixtures/file4.yaml',
                           JSON,
                           'tests/fixtures/results/nestedjson.txt'),
                          ('tests/fixtures/file1.json',
                           'tests/fixtures/file2.json',
                           STYLISH,
                           'tests/fixtures/results/flat.txt'),
                          ('tests/fixtures/file1.yml',
                           'tests/fixtures/file2.yml',
                           STYLISH,
                           'tests/fixtures/results/flat.txt'),
                          ('tests/fixtures/file1.yaml',
                           'tests/fixtures/file2.yaml',
                           STYLISH,
                           'tests/fixtures/results/flat.txt'),
                          ('tests/fixtures/file3.json',
                           'tests/fixtures/file4.json',
                           PLAIN,
                           'tests/fixtures/results/plain.txt'),
                          ('tests/fixtures/file3.yaml',
                           'tests/fixtures/file4.yaml',
                           PLAIN,
                           'tests/fixtures/results/plain.txt'),
                          ('tests/fixtures/file3.json',
                           'tests/fixtures/file4.json',
                           STYLISH,
                           'tests/fixtures/results/stylish.txt'),
                          ('tests/fixtures/file3.yaml',
                           'tests/fixtures/file4.yaml',
                           STYLISH,
                           'tests/fixtures/results/stylish.txt')])
def test_generate_diff(file1, file2, report_format, result_file):
    with open(result_file) as file:
        result = file.read()
    assert result == generate_diff(file1, file2, report_format)


def is_json(data):
    try:
        json.loads(data)
    except ValueError:
        return False
    return True


@pytest.mark.parametrize('data_file1, data_file2',
                         [('tests/fixtures/file3.json',
                           'tests/fixtures/file4.yaml'),
                          ('tests/fixtures/file3.yaml',
                           'tests/fixtures/file4.json')])
def test_generate_diff_json(data_file1, data_file2):
    result1 = generate_diff(data_file1, data_file2, JSON)
    result2 = generate_diff(data_file1, data_file2)
    assert is_json(result1) is True
    assert is_json(result2) is False
