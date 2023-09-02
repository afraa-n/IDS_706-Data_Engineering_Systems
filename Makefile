install:
	pip install --upgrade pip &&\
		pip install --prefer-binary -r requirements.txt

test:
	python -m pytest -vv --cov=main test_*.py

format:
	black *.py

lint:
	pylint $(find . -name "*.py" | xargs)

all: install lint format test