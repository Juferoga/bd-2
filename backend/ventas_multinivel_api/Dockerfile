FROM python:3.11.2-slim-bullseye
ENV PYTHONUNBUFFERED 1
RUN mkdir /code

WORKDIR /code
COPY requirements.txt /code/

RUN pip install -r requirements.txt

COPY . /code/

RUN export $(cat .env)
CMD export $(cat .env) && python manage.py runserver 0.0.0.0:80