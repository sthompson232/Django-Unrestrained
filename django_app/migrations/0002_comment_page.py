# Generated by Django 3.1.4 on 2020-12-18 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='page',
            field=models.CharField(default='undefined', max_length=100),
            preserve_default=False,
        ),
    ]
