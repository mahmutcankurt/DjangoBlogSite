# Generated by Django 2.2.4 on 2019-09-08 22:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0018_auto_20190909_0130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='author',
            field=models.CharField(max_length=150, verbose_name='Author'),
        ),
    ]
