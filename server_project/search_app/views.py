from django_elasticsearch_dsl_drf.viewsets import DocumentViewSet
from .documents import ArticleDocument
from .serializers import ArticleDocumentSerializer
from django_elasticsearch_dsl_drf.filter_backends import SearchFilterBackend, FilteringFilterBackend, SuggesterFilterBackend
from django_elasticsearch_dsl_drf.constants import SUGGESTER_COMPLETION


class ArticleDocumentView(DocumentViewSet):
    document = ArticleDocument
    serializer_class = ArticleDocumentSerializer

    filter_backends = [
        FilteringFilterBackend,
        SearchFilterBackend,
        SuggesterFilterBackend
    ]

    search_fields = (
        'title',
    )

    filter_fields = {
        'category' : 'category.id'
    }

    suggester_fields = {
        'title': {
            'field': 'title.suggest',
            'suggesters' : [
                SUGGESTER_COMPLETION
            ],
        },
    }




