# Generated by Django 3.0.8 on 2020-08-06 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_one', '0012_auto_20200725_1015'),
    ]

    operations = [
        migrations.CreateModel(
            name='Agregate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_of_controller', models.IntegerField(null=True, verbose_name='№ Контролдлера')),
                ('t_delta', models.IntegerField(null=True, verbose_name='T дельта')),
                ('t_input', models.DecimalField(decimal_places=1, max_digits=1000, null=True, verbose_name='Температура входу')),
                ('t_output', models.DecimalField(decimal_places=1, max_digits=1000, null=True, verbose_name='Температура виходу')),
                ('auto_hand', models.CharField(max_length=30, null=True)),
                ('capacity', models.DecimalField(decimal_places=1, max_digits=1000, null=True, verbose_name='Обєм')),
                ('capacity_warm', models.DecimalField(decimal_places=2, max_digits=1000, null=True, verbose_name='Обєм тепла')),
                ('capacity_current', models.DecimalField(decimal_places=1, max_digits=1000, null=True, verbose_name='Обєм поточний')),
                ('pressure', models.DecimalField(decimal_places=1, max_digits=1000, null=True, verbose_name='Тиск виходу')),
                ('digital_input', models.IntegerField(null=True, verbose_name='Цифровий вхід')),
                ('digital_output', models.IntegerField(null=True, verbose_name='Цифровий вихід')),
                ('parameters', models.IntegerField(null=True, verbose_name='T дельта')),
                ('w_accumulate', models.DecimalField(decimal_places=1, max_digits=1000, null=True, verbose_name='W накоп.')),
                ('w_current', models.DecimalField(decimal_places=1, max_digits=1000, null=True, verbose_name='W пот.')),
                ('zdate', models.DateField(null=True, verbose_name='Дата зони')),
                ('ztime', models.TimeField(null=True, verbose_name='Час зони')),
            ],
        ),
    ]