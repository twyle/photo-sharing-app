# pull the official docker image
FROM python:3.10-slim

# set work directory
WORKDIR /app

# set env variables
ENV FLASK_APP=manage.py
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# copy pylint and flake8 confis
COPY .pylintrc .
COPY setup.cfg .

# update pip
RUN pip install --upgrade pip

# install development dependencies
COPY requirements-dev.txt .
RUN pip install -r requirements-dev.txt

# install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# copy project
COPY . .

#run the linters
RUN black api/
RUN isort .
RUN flake8
RUN pydocstyle  api/
RUN pylint --rcfile=.pylintrc ./api

#run the tests
# RUN python -m pytest

EXPOSE 5000

# run server
CMD ["gunicorn", "-b", "0.0.0.0:5000", "manage:app"]