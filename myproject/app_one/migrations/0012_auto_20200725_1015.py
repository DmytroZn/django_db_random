# Generated by Django 3.0.8 on 2020-07-25 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_one', '0011_auto_20200725_0942'),
    ]

    operations = [
        migrations.AlterField(
            model_name='zone',
            name='n_zone',
            field=models.IntegerField(verbose_name='номер зони'),
        ),
    ]