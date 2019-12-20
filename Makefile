clean:
	@find . -name "*.pyc" -exec rm -rf {} \;
	@find . -name "__pycache__" -delete

test:
	pytest

flake:
	flake8

black:
	black --target-version py37 metabase_client --check
	black --target-version py37 tests --check

