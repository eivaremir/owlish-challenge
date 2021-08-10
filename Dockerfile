FROM python:alpine AS base




COPY requirements.txt .

RUN apk update \
    && apk add --virtual build-deps gcc python3-dev musl-dev \
    && apk add --no-cache mariadb-dev



RUN pip install -r requirements.txt


WORKDIR /owlish-rest
COPY . .


RUN apk del build-deps

CMD python /owlish-rest/owlish_rest/manage.py runserver 0.0.0.0:4000