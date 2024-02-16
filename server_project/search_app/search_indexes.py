from django_elasticsearch_dsl import Document
from django_elasticsearch_dsl.registries import registry
from .models import Article, ArticleDocument


# @registry.register_document
# class Arti