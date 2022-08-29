make lint:
	poetry run flake8

install:
	poetry install

build:
	poetry build

publish:
	poetry publish --dry-run

test:
	poetry run pytest

test-coverage:
	poetry run pytest --cov=xml_diff --cov-report xml