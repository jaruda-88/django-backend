#!/bin/bash

echo "Apply database migrations"
python manage.py makemigrations search_app
python manage.py migrate search_app

# echo "test data"
# python manage.py loaddata category.json article.json

echo "Start server"
python manage.py runserver 0.0.0.0:8000