# Generated by Django 5.0.6 on 2024-07-10 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(default=None, unique=True)),
                ('height', models.IntegerField(default=None)),
                ('width', models.IntegerField(default=None)),
            ],
        ),
    ]
