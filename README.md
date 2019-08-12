# Biker

Biker aims to be a web platform for biking competition. It allows users to track themselves as well as build local
communities and challenge each other.


## Development setup

This is a standard Django project. It currently runs with Python 3.5 and uses Django 2.2.4.

It is highly recommended to use a virtualenv.
```
$ git clone https://github.com/surfingdmx/biker.git
$ cd biker
$ virtualenv -p python3 venv
$ . venv/bin/activate
(venv) $ pip3 install -r requrements.txt
(venv) $ cd biker
(venv) $ python3 manage.py migrate
(venv) $ python3 manage.py createsuperuser
(venv) $ python3 manage.py runserver
```
This starts a development server on localhost:8000.

For getting started with Django see the [documentation](https://docs.djangoproject.com/en/2.2/).