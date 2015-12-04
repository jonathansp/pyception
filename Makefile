.PHONY: install test upload

install:
	pip install -r requirements.txt
	pip install -r requirements_dev.txt

test:
	coverage run setup.py test

upload: test
