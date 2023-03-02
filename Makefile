update:
	@pip install --upgrade pip

install:
	@pip install -r services/app/requirements.txt

install-dev:
	@pip install -r services/app/requirements-dev.txt

test:
	@python -m pytest

coverage:
	@coverage run -m pytest 
	@coverage report -m

run:
	@python services/app/manage.py run

lint:
	@black services/app
	@isort services/app
	@flake8
	@pydocstyle  services/app/api
	@pylint --rcfile=.pylintrc ./services/app/api