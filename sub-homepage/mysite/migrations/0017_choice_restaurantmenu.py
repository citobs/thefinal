# Generated by Django 4.0.8 on 2022-12-08 23:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0016_fullist_cr_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='choice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('res', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='RestaurantMenu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('restaurant', models.CharField(max_length=300, null=True)),
                ('menu', models.CharField(max_length=300, null=True)),
            ],
        ),
    ]
