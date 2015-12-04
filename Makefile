.PHONY: install test upload

install:
	pip install -r requirements.txt
	pip install -r requirements_dev.txt

test:
	coverage run setup.py test

upload: test

	rm -rf dist/
	rm -rf build/
	python setup.py bdist_wheel
	twine upload dist/* -I -U
