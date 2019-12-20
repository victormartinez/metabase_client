clean:
	@find . -name "*.pyc" -exec rm -rf {} \;
	@find . -name "__pycache__" -delete

test:
	pytest

flake:
	flake8 --ignore=W391,W504,W503 --max-line-length=88 metabase_client/ tests/

black:
	black --target-version py37 metabase_client --check
	black --target-version py37 tests --check

