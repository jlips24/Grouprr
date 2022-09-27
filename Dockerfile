# syntax=docker/dockerfile:1
FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY requirements.txt /code/
RUN python3 -m venv grouprr-env
RUN source grouprr-env/bin/activate
RUN pip install -r requirements.txt
COPY ./src/ /code/