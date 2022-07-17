make lint:
	poetry run flake8 xml_diff

install:
	poetry install

test-coverage:
	poetry run pytest --cov=xml_diff --cov-report xml
