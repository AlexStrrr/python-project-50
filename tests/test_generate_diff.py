from gendiff.gendiff import generate_diff
from gendiff.gendiff import make_diff


def test_gen_diff_json():
    result = generate_diff("tests/fixtures/file1.json", "tests/fixtures/file2.json")
    assert result == "tests/fixtures/results/flat.txt"


def test_gen_diff_yaml():
    result = generate_diff("tests/fixtures/file1.yml", "tests/fixtures/file2.yml")
    assert result == "tests/fixtures/results/flat.txt"


def test_make_diff():
    result = make_diff("tests/fixtures/file3.json", "tests/fixtures/file4.json")
    assert result == "tests/fixtures/results/nested.txt"
