install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest -vv --cov=main --cov=library test_*.py

format:	
	black *.py 

lint:
	ruff check library/*.py test_*.py *.py
	
all: install lint test format