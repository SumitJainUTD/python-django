from django.urls import path
from .views import article_list, home_page, article_detail, ArticleAPIView, ArticleDetailView
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
    # path('article/', article_list),
    path('', home_page),
    # path('detail/<int:pk>', article_detail),
    path('article/', ArticleAPIView.as_view()),
    path('detail/<int:id>', ArticleDetailView.as_view()),
]
