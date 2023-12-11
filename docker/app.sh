#!/bin/bash

sleep 5

python manage.py migrate

python manage.py populate_data

python manage.py add_superuser

python manage.py runserver 0.0.0.0:8000