FROM python:3.7-slim-buster

ARG minimize_css="yes"

COPY . /app
WORKDIR /app

RUN pip install -r requirements.txt

RUN if [ "$minimize_css" = "yes" ] ; then python minimize.py ; fi

RUN msgfmt locale/en_US/LC_MESSAGES/en.po -o locale/en_US/LC_MESSAGES/en.mo

EXPOSE 8080
cmd ["python", "server.py"]
