import json
from gendiff.run.gendiff import generate_diff
import pytest


@pytest.mark.parametrize('data_file1, data_file2, result_file',
                         [('tests/fixtures/file1.json',
                           'tests/fixtures/file2.json',
                           'tests/fixtures/results/flat.txt'),
                          ('tests/fixtures/file1.yml',
                           'tests/fixtures/file2.yml',
                           'tests/fixtures/results/flat.txt'),
                          ('tests/fixtures/file1.yaml',
                           'tests/fixtures/file2.yaml',
                           'tests/fixtures/results/flat.txt')])
def test_generate_diff_flat(data_file1, data_file2, result_file):
    result = open(result_file, 'r').read()
    assert generate_diff(data_file1, data_file2) == result


@pytest.mark.parametrize('data_file1, data_file2, result_file',
                         [('tests/fixtures/file3.json',
                           'tests/fixtures/file4.json',
                           'tests/fixtures/results/stylish.txt'),
                          ('tests/fixtures/file3.yaml',
                           'tests/fixtures/file4.yaml',
                           'tests/fixtures/results/stylish.txt')])
def test_generate_diff_stylish(data_file1, data_file2, result_file):
    result = open(result_file, 'r').read()
    assert generate_diff(data_file1, data_file2) == result


@pytest.mark.parametrize('data_file1, data_file2, result_file',
                         [('tests/fixtures/file3.json',
                           'tests/fixtures/file4.json',
                           'tests/fixtures/results/plain.txt'),
                          ('tests/fixtures/file3.yaml',
                           'tests/fixtures/file4.yaml',
                           'tests/fixtures/results/plain.txt')])
def test_generate_diff_plain(data_file1, data_file2, result_file):
    result = open(result_file, 'r').read()
    assert generate_diff(data_file1, data_file2) == result


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
    result1 = generate_diff(data_file1, data_file2, 'json')
    result2 = generate_diff(data_file1, data_file2)
    assert is_json(result1) is True
    assert is_json(result2) is False
