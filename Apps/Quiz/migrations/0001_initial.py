# Generated by Django 3.1.5 on 2021-05-28 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Quizs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('gender', models.CharField(blank=True, max_length=50, null=True)),
                ('issue', models.CharField(blank=True, max_length=500, null=True)),
                ('img', models.ImageField(blank=True, null=True, upload_to='issue/')),
            ],
        ),
    ]