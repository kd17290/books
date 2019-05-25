# Books sample project

A sample project to illustrate implementing REST APIs with django.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.
### Prerequisites

1) python 3.7.3
```
https://www.python.org/downloads/
```

2) pipenv
```
pip install pipenv
```

### Installing

A step by step series of examples that tell you how to get a development env running

Clone the project:
```
git clone <git URL>
```

Change directory to cloned project:
```
cd books
```

Create virtual env and pull python version:
```
pipenv shell
```

Install pip dependecies in virtaulenv:
```
pipenv install
```
Migrate database:
```
python manage.py migrate
```
runserver:
```
python manage.py runserver
```

## Running the tests

for running automated tests
```
python manage.py test
```
This step should pass all testcases.

## Checking APIs in postman

- Import postman collection from ./documentation/books.postman_collection.json in your postman client.

- This will give you all the APIs in your postman and you can check them one by one.