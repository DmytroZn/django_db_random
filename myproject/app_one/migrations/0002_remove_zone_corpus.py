# Generated by Django 3.0.8 on 2020-07-24 10:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_one', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='zone',
            name='corpus',
        ),
    ]