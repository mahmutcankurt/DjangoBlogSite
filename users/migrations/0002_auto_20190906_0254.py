# Generated by Django 2.2.4 on 2019-09-05 23:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='email_confirmed',
            new_name='is_merchant',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='bio',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='location',
        ),
        migrations.AddField(
            model_name='profile',
            name='address',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='child_amount',
            field=models.PositiveSmallIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='locatity',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='postal_code_3',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='postal_code_4',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='birth_date',
            field=models.DateField(null=True),
        ),
    ]
