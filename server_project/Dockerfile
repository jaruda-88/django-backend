FROM python:3.11

ENV PYTHONUNBUFFERED=1

WORKDIR /server_project/

COPY requirements.txt .
COPY docker-entrypoint.sh .

RUN apt-get update && \
    apt-get install -y && \
    pip install --upgrade pip && \
    pip install --no-cache-dir --upgrade -r requirements.txt

RUN chmod +x docker-entrypoint.sh
ENTRYPOINT ["./docker-entrypoint.sh"]

COPY . /server_project

EXPOSE 8000

# CMD ["python", "manage.py", "makemigrations", 'search_app']
# CMD ["python", "manage.py", "migrate", 'search_app']
# CMD ["python", "manage.py", "loaddata", "category.json", "article.json"]
# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

