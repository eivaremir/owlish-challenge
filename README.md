# owlish-challenge

Welcome, thanks for the opportunity. Find the guidelines below:

There are 2 options to get this code up and running:
- Docker
- Get the code and run locally


## Run Locally

1. Clone this repository on your local machine
2. In the root directory:
    - run `pip install -r requirements.txt` to install dependencies
    - run `python ./owlish_rest/manage.py runserver 0.0.0.0:4000` to start the server in the port 4000 or any port of your preference.

### Django management commands

__importcsv **filename**.csv__ to import a csv file into the customers table in the database, the file must contain the following columns in the same order:

| id | first_name | last_name | email | gender | company | city | title |
|----|------------|-----------|-------|--------|---------|------|-------|

__setcoords__ to fetch all customer coordinates using Google Cloud's GeoCodeAPI

## The Docker way

1. You need to be on a docker ready machine
2. 

