# Generated by Django 2.1.5 on 2019-01-06 04:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_auto_20190105_1721'),
    ]

    operations = [
        migrations.AlterField(
            model_name='keyword',
            name='keyword',
            field=models.CharField(max_length=200, null=True, verbose_name='검색 단어'),
        ),
    ]
