FROM python:alpine AS base




COPY requirements.txt .
RUN pip install -r requirements.txt


WORKDIR /owlish-rest
COPY . .

CMD python /owlish-rest/owlish_rest/manage.py runserver 0.0.0.0:8000