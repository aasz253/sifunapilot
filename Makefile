.PHONY: install dev test lint format typecheck security clean

install:
	pip install -e .

dev:
	pip install -e ".[dev]"

test:
	pytest

lint:
	ruff check .

format:
	ruff format .

typecheck:
	mypy src/

security:
	bandit -r src/
	pip-audit

clean:
	rm -rf build dist *.egg-info __pycache__ .pytest_cache .mypy_cache
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
