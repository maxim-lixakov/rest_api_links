# Generated by Django 3.2.3 on 2021-05-19 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='url_table',
            name='id',
        ),
        migrations.AlterField(
            model_name='url_table',
            name='shorten_url',
            field=models.CharField(max_length=30, primary_key=True, serialize=False),
        ),
    ]
