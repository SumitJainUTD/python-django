from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from .models import Article
from .serializers import ArticleSerializer
import json


# Create your views here.


def article_list(request):
    if request.method == 'GET':
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return JsonResponse(serializer.data, safe=False)


def home_page(request):
    if request.method == 'GET':
        x = '{ "title":"home page", "description":"This is a home page"}'
        y = json.loads(x)
        # serializer = ArticleSerializer(y, many=True)
        return JsonResponse(y, safe=False)
