# Generated by Django 4.0.8 on 2022-12-07 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0008_resultall'),
    ]

    operations = [
        migrations.CreateModel(
            name='count',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cnt', models.IntegerField(null=True)),
            ],
        ),
    ]
