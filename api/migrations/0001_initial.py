# Generated by Django 4.2 on 2023-09-11 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Persons',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('nationality', models.CharField(max_length=200)),
                ('state_of_origin', models.CharField(max_length=200)),
                ('occupation', models.CharField(max_length=200)),
            ],
        ),
    ]
