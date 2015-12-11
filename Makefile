.PHONY: install test upload

install:
	pip install -r requirements.txt
	pip install -r requirements_dev.txt

test:
	coverage run --source pyception setup.py test
	coverage report -m

upload: test

	rm -rf dist/
	rm -rf build/
	python setup.py bdist_wheel
	twine upload dist/* -u $TWINE_USER -p "$TWINE_PWD"
