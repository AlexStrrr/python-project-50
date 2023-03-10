install:
	poetry install

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

all:
	poetry update
	poetry build
	poetry publish --dry-run
	python3 -m pip install --user --force-reinstall dist/*.whl

uninstall:
	python3 -m pip uninstall hexlet-code

test:
	poetry run pytest

lint:
	poetry run flake8 gendiff

test-coverage:
	poetry run pytest --cov=gendiff tests --cov-report xml

selfcheck:
	poetry check

check:
	poetry check
	poetry run pytest
	poetry run flake8 gendiff
