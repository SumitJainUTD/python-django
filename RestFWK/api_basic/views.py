from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import Article
from .serializers import ArticleSerializer
import json


# Create your views here.

@csrf_exempt
def article_list(request):
    if request.method == 'GET':
        print("get call ARTICLE")
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        print("post call Article")
        data = JSONParser().parse(request)
        serializer = ArticleSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)



def home_page(request):
    if request.method == 'GET':
        x = '{ "title":"home page", "description":"This is a home page"}'
        y = json.loads(x)
        # serializer = ArticleSerializer(y, many=True)
        return JsonResponse(y, safe=False)
