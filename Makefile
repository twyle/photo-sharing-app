update:
	@pip install --upgrade pip

install:
	@pip install -r services/app/requirements.txt

run:
	@python services/app/manage.py run