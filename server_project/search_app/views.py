from django_elasticsearch_dsl_drf.viewsets import DocumentViewSet
from .documents import ArticleDocument
from .serializers import ArticleDocumentSerializer
from django_elasticsearch_dsl_drf.filter_backends import SearchFilterBackend


class ArticleDocumentView(DocumentViewSet):
    document = ArticleDocument
    serializer_class = ArticleDocumentSerializer

    filter_backends = [
        SearchFilterBackend
    ]

    search_fields = ('title',)




