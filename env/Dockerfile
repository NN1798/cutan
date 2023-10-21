FROM python:3.9-alpine3.17

COPY requirements.txt /temp/requirements.txt

COPY cutan /cutan
WORKDIR /cutan
EXPOSE 8000

RUN pip install -r /temp/requirements.txt

RUN apk add postgresql-client build-base postgresql-dev

RUN adduser --disabled-password service-user

USER service-user