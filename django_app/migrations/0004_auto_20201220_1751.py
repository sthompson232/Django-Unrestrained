# Generated by Django 3.1.4 on 2020-12-20 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_app', '0003_fredquerydata'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fredquerydata',
            name='end_date',
            field=models.DateField(max_length=50),
        ),
        migrations.AlterField(
            model_name='fredquerydata',
            name='start_date',
            field=models.DateField(max_length=50),
        ),
    ]
