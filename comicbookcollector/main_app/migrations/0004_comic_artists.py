# Generated by Django 4.0.4 on 2022-05-18 23:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_artist_alter_reading_options_alter_reading_end_page_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='comic',
            name='artists',
            field=models.ManyToManyField(to='main_app.artist'),
        ),
    ]
