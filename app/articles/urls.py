from django.urls import path

from .feeds import KeywordFeed, WriterFeed
from .views import article_detail, index, create_feed_url

app_name = 'articles'
urlpatterns = [
    path('', index, name='index'),
    path('search/', create_feed_url, name='search'),
    path('detail/<pk>/', article_detail, name='article-detail'),
    path('feeds/keyword/<keyword>/', KeywordFeed(), name='feeds-keyword'),
    path('feeds/writer/<user_id>/', WriterFeed(), name='feeds-writer'),
]
