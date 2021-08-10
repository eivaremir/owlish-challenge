# owlish-challenge

Welcome, thanks for the opportunity. Find the guidelines below:

There are 3 options to get this code up and running:
- Docker
- Build the docker image
- Get the code and run locally

## Docker

You need to be on a docker ready machine

1. on the CLI, run `docker pull eivaremir/owlish:latest` to pull the docker image
2. Run `docker run -d -p 80:80 --name "owlish-rest-api" eivaremir/owlish` to run it on your localhost in port 80
3. Ready, you have just deployed the REST API locally

## Build the docker image

1. In the root directory, where the Dockerfile is located, run `docker build -t owlish .`
2. Run `docker run -d -p 80:80 --name "owlish-rest-api" eivaremir/owlish` to run it on your localhost in port 80
3. Ready, you have just deployed the REST API locally


## Run Locally

1. Clone this repository on your local machine
2. In the root directory:
    - run `pip install -r requirements.txt` to install dependencies
    - run `python ./owlish_rest/manage.py runserver 0.0.0.0:80` to start the server in the port 80 or any port of your preference.
    
### Django management commands
   - __importcsv *filename*.csv__ to import a csv file into the customers table in the database, the file must contain the following columns in the same order:
    
   | id | first_name | last_name | email | gender | company | city | title |
   |----|------------|-----------|-------|--------|---------|------|-------|

   - __setcoords__ to fetch all customer coordinates using Google Cloud's GeoCodeAPI



