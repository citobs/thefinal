# Generated by Django 4.0.8 on 2022-12-10 00:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0020_choice_season_choice_weather'),
    ]

    operations = [
        migrations.AddField(
            model_name='choice',
            name='comment',
            field=models.CharField(max_length=300, null=True),
        ),
    ]
