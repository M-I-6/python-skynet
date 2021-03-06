build:
	python -m compileall ./siaskynet

install:
	python -m pip install pipenv
	pipenv install --dev

lint:
	flake8 siaskynet/ --count --show-source --statistics --per-file-ignores='__init__.py:F401'
	pylint siaskynet/ -d invalid-name,protected-access

test:
	pytest
