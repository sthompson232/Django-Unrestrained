# Generated by Django 3.1.4 on 2020-12-29 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_app', '0007_filmratings'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filmratings',
            name='rating',
            field=models.IntegerField(),
        ),
    ]