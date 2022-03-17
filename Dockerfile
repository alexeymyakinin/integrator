FROM python:3.10-slim

WORKDIR /usr/src/app

RUN apt update && apt upgrade -y
RUN apt install -y gcc postgresql postgresql-contrib
RUN pip install -U setuptools

COPY . .

RUN pip install -r requirements.txt