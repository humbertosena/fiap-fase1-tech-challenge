.PHONY: install lint test run-api clean

install:
	uv sync --all-extras

lint:
	uv run ruff check . --fix

test:
	uv run pytest tests/

run-api:
	uv run uvicorn src.api.main:app --reload --host 0.0.0.0 --port 8000

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	rm -rf .pytest_cache .ruff_cache mlruns/ .venv/
