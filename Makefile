all: flake8 mypy

flake8:
	flake8

mypy:
	for file in */*.py; do \
		mypy $$file ; \
	done