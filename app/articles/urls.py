from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from .feed import KeywordFeed, WriterFeed, MyFeed
from .views import article_detail, index, search

app_name = 'articles'
urlpatterns = [
    path('', index, name='index'),
    path('search/', search, name='search'),
    path('detail/<pk>/', article_detail, name='article-detail'),
    path('feeds/keyword/<keyword>/', KeywordFeed(), name='feeds-keyword'),
    path('feeds/writer/<user_id>/', WriterFeed(), name='feeds-writer'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
