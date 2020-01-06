init:
	./.venv/bin/python setup.py bdist_wheel

install:
	virtualenv ./.venv
	./.venv/bin/pip install -r requirement.txt

unittest:
	./.venv/bin/python -m unittest discover tests

coverage:
	./.venv/bin/coverage run -m unittest discover tests
	./.venv/bin/coverage html
	./.venv/bin/coverage report

