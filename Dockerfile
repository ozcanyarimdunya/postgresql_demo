FROM python:3.6.4

ENV PYTHONBUFFERED 1

COPY requirements.txt /code/requirements.txt
WORKDIR /code

RUN pip install -r requirements.txt

COPY . /code
WORKDIR /code
