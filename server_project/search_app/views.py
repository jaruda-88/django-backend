from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import generics
from .models import Article
from .serializers import ArticleSerializer
from elasticsearch_dsl import connections, Q


# class ArticleListCreateAPIVIEW(generics.ListCreateAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer

# def search(request):
#     query = request.GET.get('query', '')

#     s = Article.search().queyr(
#         Q('multi_match', query=query, fields=["title", "content"])
#     )

#     response = s.execute()
#     articles = [hit.to.dict() for hit in response]

#     return JsonResponse(articles, safe=False)


# class ArticleView(viewsets.ModelViewSet):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer

#     def get_queryset(self):
#         title = self.request.query_params.get("title")
#         category = self.request.query_params.get("category")

#         query = Q()

#         if title:
#             query &= Q(title=title)
#         if category:
#             query &= Q(category=category)
        
#         queryset = Article.objects.filter(query)

#         return queryset

