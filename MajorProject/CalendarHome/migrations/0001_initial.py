# Generated by Django 4.1.6 on 2023-03-10 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='university_activities',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(max_length=20)),
                ('end_date', models.DateField(max_length=20)),
                ('university_name', models.CharField(max_length=200)),
                ('university_activity', models.CharField(max_length=200)),
            ],
        ),
    ]
