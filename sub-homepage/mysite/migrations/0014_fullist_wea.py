# Generated by Django 4.0.8 on 2022-12-08 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0013_rename_emotion_fullist_emot_rename_seaon_fullist_sea'),
    ]

    operations = [
        migrations.AddField(
            model_name='fullist',
            name='wea',
            field=models.CharField(default=(), max_length=300),
            preserve_default=False,
        ),
    ]
