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