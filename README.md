# sourcemanager
[![CI](https://github.com/Project-MNET/sourcemanager/actions/workflows/main.yml/badge.svg?branch=main)](https://github.com/Project-MNET/sourcemanager/actions)

[![codecov](https://codecov.io/github/Project-MNET/sourcemanager/graph/badge.svg?token=2YKCU8Z9FR)](https://codecov.io/github/Project-MNET/sourcemanager)

A program to chart, manage, and view sources/references.

This project is licensed under the terms of the GNU GPLv3 license.

## [Link to backlog](https://docs.google.com/spreadsheets/d/1BsAK4wQ-Yx5VGymUslDFWsJHH8hVnQ3YN_gs9V_qJI8/edit?usp=sharing)

## Definition of Done (DoD):
- Testit läpäisty
- Koodi tarkastettu
- Hyväksyntäkriteerit ovat täyttyneet
- Asiakas hyväksyy User Storyn

## Installation instructions:
Includes some example commands that may or may not work, depending on your machine.

Clone the repository. 
```
git clone https://github.com/Project-MNET/sourcemanager.git
```
Navigate to the cloned directory.
```
cd sourcemanager
```
Install poetry.
```
poetry install
```
Move to the src directory.
```
cd src
```
You should now be able to start the source manager.
```
poetry run flask run
```
##  Docker POSTGRESQL DATABASE Installation Instructions.
Download Docker Desktop, the program has to be running when the database is being used.

Create the .env file in the project root directory.
```
nano .env
```
Paste the following into the .env file:
```
POSTGRES_USER={USERNAME}
POSTGRES_PASSWORD={PASSWORD}
POSTGRES_DB=flask_db
SECRET_KEY=1234

DATABASE_URL=postgresql+psycopg2://{USERNAME}:{PASSWORD}@localhost:5432/flask_db
```
Choose a username and a password and insert them into the .env file:

POSTGRES_USER={your chosen username}

POSTGRES_PASSWORD={your chosen password}

Make sure to also edit the database URL to include your chosen username and password.

For example:
```
POSTGRES_USER=Gabriel
POSTGRES_PASSWORD=Gabe12
POSTGRES_DB=flask_db
SECRET_KEY=1234

DATABASE_URL=postgresql+psycopg2://Gabriel:Gabe12@localhost:5432/flask_db
```
Run Docker:
```
docker compose up -d
```
Now the database has been created and initialized. The program can be run with the following command in the src directory:
```
poetry run flask run
```
The software should automatically create a database in your Docker and the tables and create a test column in there.
Then, it should print the test column in the console.

Database functions need to be used with app context in this style:  
```
with app.app_context():  
    database.esim()
```
##  Resetting the database

If you run in to trouble with the database, you may reset it in the following way:
```
docker compose down -v
```
Reinitialize database:
```
docker compose up -d
```


