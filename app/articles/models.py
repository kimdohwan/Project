from django.db import models


class Keyword(models.Model):
    keyword = models.CharField(verbose_name='검색 단어', null=True, max_length=200)


class Writer(models.Model):
    user_id = models.CharField(verbose_name='작가ID', null=False, max_length=200, unique=True)
    media_name = models.CharField(verbose_name='작가명', null=False, max_length=200)
    num_subscription = models.IntegerField(verbose_name='구독자 수', null=True)


class Article(models.Model):
    title = models.CharField(verbose_name='제목', null=False, max_length=200)
    content = models.TextField(verbose_name='본문', null=False)
    article_txid= models.CharField(verbose_name='작가id_글번호', null=False, unique=True, max_length=200)
    published_time = models.DateTimeField()
    text_id = models.IntegerField(verbose_name='글 번호', null=False)
    writer = models.ForeignKey(
        Writer,
        on_delete=models.CASCADE,
        related_name='articles'
    )
    keyword = models.ManyToManyField(
        Keyword,
        related_name='articles',
    )
