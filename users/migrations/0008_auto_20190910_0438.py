# Generated by Django 2.2.4 on 2019-09-10 01:38

from django.db import migrations, models
import users.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20190910_0357'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_photo',
            field=models.ImageField(default='profile_photo/default/user-default.jpg', upload_to=users.models.upload_to, verbose_name='Profile Photo'),
        ),
    ]
