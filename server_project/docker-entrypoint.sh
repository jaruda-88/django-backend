#!/bin/bash

containerid=$1

echo "apply fixture data"
docker exec -it $containerid python manage.py loaddata article.json category.json

echo "elasticsear init index"
docker exec -it $containerid python manage.py search_index --rebuild

# dockerize -wait tcp://es:9200 -timeout 20s

# echo "Apply database migrations"
# python manage.py makemigrations search_app
# python manage.py migrate search_app

# echo "test data"
# python manage.py loaddata article.json category.json

# echo "Start server"
# python manage.py runserver 0.0.0.0:8000 