FROM python:3.11

ENV PYTHONUNBUFFERED=1

WORKDIR /server_project/

COPY requirements.txt .

RUN apt-get update && \
    apt-get install -y && \
    pip install --upgrade pip && \
    pip install --no-cache-dir --upgrade -r requirements.txt
