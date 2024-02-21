- pip install django
- pip install djangorestframework
- pip install elasticsearch
- pip install elasticsearch-dsl
- pip install django-elasticsearch-dsl
- pip install django-elasticsearch-dsl-drf

# nori 
## local mac
- brew install elastic/tap/elasticsearch-full
- (path)/usr/local/Cellar/elasticsearch-full/7.8.1/bin
- elasticsearch-plugin install analysis-nori

## docker 
-python manage.py search_index --rebuild
-python nange.py loaddata article.json category.json

-http://localhost:8000/search_app?search=a
-http://localhost:8000/search_app?category=2
-http://localhost:8000/search_app/suggest/?title__completion=how


