FROM python:3.8.3-alpine

WORKDIR /usr/src/api

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev

RUN pip install pipenv

COPY ./Pipfile .
COPY ./Pipfile.lock .

RUN pipenv install
RUN pipenv install --system

COPY ./entrypoint.sh .
COPY . .
RUN chmod +x ./entrypoint.sh

ENTRYPOINT ["/usr/src/api/entrypoint.sh"]