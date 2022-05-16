# Generated by Django 4.0.4 on 2022-05-16 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('series', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=100)),
                ('issue_num', models.IntegerField()),
                ('publisher', models.CharField(max_length=100)),
                ('year', models.IntegerField()),
            ],
        ),
    ]