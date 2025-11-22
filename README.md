# sourcemanager
[![CI](https://github.com/Project-MNET/sourcemanager/actions/workflows/main.yml/badge.svg?branch=main)](https://github.com/Project-MNET/sourcemanager/actions)

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
Troubleshooting:  
If you run into issues with importing the forms module, change the 5th line of app.py to
"from .forms import ReferenceForm" instead of "from forms import ReferenceForm".
```
nano app.py
```
## INSTALLATION INSTRUCTIONS FOR DOCKER POSTGRESQL DATABASE.
First download docker desktop software.
Docker Desktop has to be on when the database is being used.

Create .env file in the project directory (Above src) with the command 
```
touch .env
```
ADD The information that is in {} and remove the brackets after. 
POSTGRES_USER={NAME}
POSTGRES_PASSWORD={PASSWORD}
POSTGRES_DB=flask_db
DATABASE_URL=postgresql+psycopg2://{NAME}:{PASSWORD}@localhost:5432/flask_db

Make sure that the Name and PASSWORD sections match
run docker with the command 
```
docker compose up -d
```
This runs docker in the background and then you can start flask from the src directory with: 
```
poetry run flask run
```
The software should automatically create a database in your docker and the tables and create a test column in there.
Then it should print the test column in the console.

Database funktions need to be used with app context in this style:
with app.app_context():
    database.esim()
    
