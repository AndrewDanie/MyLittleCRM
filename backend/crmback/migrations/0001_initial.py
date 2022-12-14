# Generated by Django 4.1 on 2022-08-10 16:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_name', models.CharField(max_length=200, verbose_name='Клиент')),
                ('device_type', models.CharField(max_length=200, verbose_name='Тип устройства')),
                ('date_start', models.DateField(blank=True, null=True, verbose_name='Дата начала работ')),
                ('date_finish', models.DateField(blank=True, null=True, verbose_name='Дата окончания работ')),
                ('master_name', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Мастер')),
            ],
        ),
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(verbose_name='Название работы')),
                ('price', models.IntegerField(verbose_name='Стоимость работы')),
                ('order', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='crmback.order')),
            ],
        ),
        migrations.CreateModel(
            name='Spare_part',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(verbose_name='Наименование запчасти')),
                ('price', models.IntegerField(verbose_name='Стоимость запчасти')),
                ('order', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='crmback.order')),
            ],
        ),
        migrations.CreateModel(
            name='Income',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_time', models.DateTimeField(verbose_name='Время поступления денег')),
                ('amount', models.IntegerField(verbose_name='Поступленные средства')),
                ('order', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='crmback.order')),
            ],
        ),
        migrations.CreateModel(
            name='Defect',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(verbose_name='Описание дефекта')),
                ('order', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='crmback.order')),
            ],
        ),
    ]
