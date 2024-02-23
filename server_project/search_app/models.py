from django.db import models
from elasticsearch_dsl import Document, Text, Keyword
from server_project.settings import AUTH_USER_MODEL


class Category(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Article(models.Model):
    title = models.CharField(max_length=100)
    category = models.ForeignKey(
        Category, related_name='category', on_delete=models.CASCADE
    )

    def __str__(self):
        return self.title