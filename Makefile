
SHELL := /bin/bash

.SILENT: clean
.IGNORE: clean

# build the package from the source
build:
	python -m build
	twine check --strict dist/*

clean:
	rm -rf build/
	rm -rf dist/
	rm -rf src/bloodfeather.egg-info/
	rm -rf venv/
	rm -rf `find . -type d -name __pycache__`

# create a development environment
devenv:	build 
	python -m venv venv/
	. venv/bin/activate; pip install -e .

