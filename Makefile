update:
	@pip install --upgrade pip

install:
	@pip install -r services/app/requirements.txt

install-dev:
	@pip install -r services/app/requirements-dev.txt

test:
	@python -m pytest --disable-warnings

coverage:
	@coverage run -m pytest --disable-warnings
	@coverage report -m

run:
	@python services/app/manage.py run

gunicorn:
	@cd services/app && gunicorn -b 0.0.0.0:5000 manage:app

lint:
	@black services/app
	@isort services/app
	@flake8
	@pydocstyle  services/app/api
	@pylint --rcfile=.pylintrc ./services/app/api

build-dev:
	@docker build -f ./services/app/Dockerfile -t photo-sharing-app-dev:latest ./services/app

run-dev:
	@docker run -p5000:5000 --env-file=./services/app/.env photo-sharing-app-dev:latest

build-prod:
	@docker build -f ./services/app/Dockerfile.prod -t photo-sharing-app-prod:latest ./services/app

run-prod:
	@docker run -p5000:5000 --env-file=./services/app/.env photo-sharing-app-prod:latest

dev:
	@docker-compose -f docker-compose-dev.yaml up --build