# photo-sharing-app

> An application for sharing photos with your friends.

<p align="center">
  <img title="Bandit badge" alt="Bandit badge" src="https://github.com/twyle/Medium-Clone-Blog-Service/actions/workflows/feature-development-workflow.yml/badge.svg" />
  <img title="Bandit badge" alt="Bandit badge" src="https://github.com/twyle/Medium-Clone-Blog-Service/actions/workflows/development-workflow.yml/badge.svg" />
  <img title="Bandit badge" alt="Bandit badge" src="https://github.com/twyle/Medium-Clone-Blog-Service/actions/workflows/staging-workflow.yml/badge.svg" />
  <img title="Bandit badge" alt="Bandit badge" src="https://github.com/twyle/Medium-Clone-Blog-Service/actions/workflows/release-workflow.yml/badge.svg" />
  <img title="Bandit badge" alt="Bandit badge" src="https://github.com/twyle/Medium-Clone-Blog-Service/actions/workflows/production-workflow.yml/badge.svg" />
  <img title="Bandit badge" alt="Bandit badge" src="https://img.shields.io/badge/security-bandit-yellow.svg" />
  <img title="Bandit badge" alt="Bandit badge" src="https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336" />
  <img title="Bandit badge" alt="Bandit badge" src="https://img.shields.io/badge/Made%20with- Python-1f425f.svg" />
  <img title="Bandit badge" alt="Bandit badge" src="https://img.shields.io/github/license/Naereen/StrapDown.js.svg" />
  <img title="Bandit badge" alt="Bandit badge" src="https://img.shields.io/badge/Medium-12100E?style=flat&logo=medium&logoColor=white" />
  <img title="Bandit badge" alt="Bandit badge" src="https://img.shields.io/badge/github%20actions-%232671E5.svg?style=flat&logo=githubactions&logoColor=white" />
  <img title="Bandit badge" alt="Bandit badge" src="https://img.shields.io/badge/flask-%23000.svg?style=flat&logo=flask&logoColor=white" />
  <img title="Bandit badge" alt="Bandit badge" src="https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=flat&logo=visual-studio-code&logoColor=white" />
  <img title="Bandit badge" alt="Bandit badge" src="https://img.shields.io/badge/Ubuntu-E95420?style=flat&logo=ubuntu&logoColor=white" />
  <img title="Bandit badge" alt="Bandit badge" src="https://img.shields.io/badge/gunicorn-%298729.svg?style=flat&logo=gunicorn&logoColor=white" />
</p>

## Application Overview

This is a social application that enables an authenticated and authorized user to share images and short messages with their friends. It is a responsive single page application built with python,flask, html, javascript and css.

<img src="assets/images/photo-sharing-app.png" class="img-responsive" alt="">

## Application Demo

The application supports the following operations:

1. Account creation using a username and email address.
2. Logging in and out
3. Updating user information including he user password.
4. Creating, viewing, deleting and updating posts which consist of an image andsome text.
5. Reacting to posts, including liking and commenting.
6. Sending private messages to other users.

<p align=center>
  <img src="assets/videos/social-media-app.gif" />
</p>

## Local Setup

To work with the application locally, first make sure the following are present:

1. An AWS account, with the secret key and acess key.
2. An s3 bucket with write and read permission.
3. Docker and docker-compose are locally installed.
4. Optionally an email address and email provider this project uses AWS SESS.

Folow these steps to start the application:

1. Clone the project repo:

  ```sh
  git clone https://github.com/twyle/photo-sharing-app.git
  ```

2. Navigate to the project directory, then create the project secrets:

  ```sh
  cd photo-sharing-app
  touch ./services/app/.env
  ```

  And then paste the following:
  ```sh
  FLASK_DEBUG=True
  FLASK_ENV=development
  FLASK_APP=manage.py 
  SECRET_KEY=secret-key 
  POSTGRES_HOST=localhost
  POSTGRES_USER=lyle
  POSTGRES_PASSWORD=lyle
  POSTGRES_DB=lyle
  POSTGRES_PORT=5432
  S3_BUCKET=<s3-bucket-name>
  AWS_ACCESS_KEY=<aws-access-key>
  AWS_ACCESS_SECRET=<aws-secret-key>
  CELERY_BROKER_URL=
  CELERY_RESULT_BACKEND
  LOGGER_HOST=<ip-address>
  LOGGER_PORT=
  ```

3. Start the logging service:
  ```sh
  docker-compose up -f services/logging/docker-compose.yml --build -d
  ```

  This takes a while

4. Start the application:
  ```sh
  docker-compose -f docker-compose-dev up --build -d
  ```

5. Navigate to ```flask.localhost``` to see the application.

## Deployment

The application is containerized and deployed to AWS EC2. It uses AWS Route53 to direct traffic to an EC2 instance with docker and docker-compose installed. It uses traefik as a everse proxy. AWS S3 is used for image storage, AWS Postgres for data storage and these resources are provided using terraform.

<img src="assets/images/search_service.png" class="img-responsive" alt="">

## Author :black_nib:

* **Lyle Okoth** <[twyle](https://github.com/twyle)>