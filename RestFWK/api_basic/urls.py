from django.urls import path
from .views import article_list, home_page

urlpatterns = [
    path('article/', article_list),
    path('', home_page),
]