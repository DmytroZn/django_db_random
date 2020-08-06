# Generated by Django 3.0.8 on 2020-07-24 10:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Corpus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_corpus', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Zone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('n_zone', models.IntegerField(verbose_name='номер зони')),
                ('corpus', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_one.Corpus')),
            ],
        ),
        migrations.CreateModel(
            name='Agregat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('n_zag', models.CharField(blank=True, max_length=40, verbose_name='гос номер')),
                ('n_agr', models.IntegerField(verbose_name='номер агрегата')),
                ('corpus', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_one.Corpus')),
                ('n_zone', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_one.Zone')),
            ],
        ),
    ]
