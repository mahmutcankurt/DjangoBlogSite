# Generated by Django 2.2.4 on 2019-09-06 21:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20190906_2145'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='child_amount',
        ),
    ]