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
