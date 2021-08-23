# Generated by Django 3.2.6 on 2021-08-23 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=80)),
                ('description', models.TextField(max_length=600)),
                ('start_time', models.DateTimeField()),
                ('end_tie', models.DateTimeField()),
            ],
        ),
    ]