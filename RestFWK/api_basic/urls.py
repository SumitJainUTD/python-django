from django.urls import path
from .views import article_list, home_page
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
    path('article/', article_list),
    path('', home_page),
]
