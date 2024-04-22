FROM python:3.11-slim

RUN mkdir /docker
WORKDIR /docker

COPY requirements.txt /docker/
RUN pip install -r requirements.txt
COPY . /docker/

CMD python manage.py runserver 0.0.0.0:8000
