FROM python:alpine AS base

COPY requirements.txt .
RUN pip install -r requirements.txt


WORKDIR /app
COPY . .

CMD python /app/app/manage.py