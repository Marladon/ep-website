FROM python:3.7-slim-buster

COPY . /app
WORKDIR /app

RUN pip install -r requirements.txt && \
    python minimize.py && \
    apt-get update && \
    apt-get install -y gettext && \
    apt-get clean && rm -rf /var/cache/apt/* && rm -rf /var/lib/apt/lists/* && rm -rf /tmp/* && \
    msgfmt locale/en_US/LC_MESSAGES/en.po -o locale/en_US/LC_MESSAGES/en.mo

EXPOSE 8080
cmd ["python", "server.py"]
