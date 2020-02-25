# Generated by Django 3.0.3 on 2020-02-25 15:48

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MessageStock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=15, null=True)),
                ('surname', models.CharField(blank=True, max_length=20, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=12, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')])),
                ('email', models.EmailField(help_text='A valid email please', max_length=254)),
                ('message', models.TextField(default='')),
            ],
            options={
                'verbose_name': 'wiadomość',
                'verbose_name_plural': 'wiadomości',
            },
        ),
        migrations.CreateModel(
            name='Segment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('segment', models.CharField(blank=True, max_length=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CarStock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=15)),
                ('year', models.CharField(blank=True, max_length=4, null=True)),
                ('eng_cap', models.CharField(blank=True, max_length=4, null=True)),
                ('description', models.TextField(default='')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='')),
                ('price', models.CharField(blank=True, max_length=4, null=True)),
                ('segment', models.ManyToManyField(related_name='car_segment', to='main.Segment')),
            ],
            options={
                'verbose_name': 'samochód',
                'verbose_name_plural': 'samochody',
            },
        ),
    ]
