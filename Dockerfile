FROM python:3.7-slim-buster

COPY . /app
WORKDIR /app

RUN pip install -r requirements.txt
RUN apt-get update && apt-get install -y sqlite3

EXPOSE 8000
cmd ["python", "manage.py", "runserver"]
