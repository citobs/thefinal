# Generated by Django 4.1.2 on 2022-12-01 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0006_alter_post_mainphoto'),
    ]

    operations = [
        migrations.CreateModel(
            name='MenuScoreAll',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('menu', models.TextField(blank=True, null=True)),
                ('restaurant', models.TextField(blank=True, null=True)),
                ('happy_winter', models.FloatField(blank=True, null=True)),
                ('happy_winter_snow', models.FloatField(blank=True, null=True)),
                ('happy_winter_rain', models.FloatField(blank=True, null=True)),
                ('happy_fall', models.FloatField(blank=True, null=True)),
                ('happy_fall_rain', models.FloatField(blank=True, null=True)),
                ('happy_summer', models.FloatField(blank=True, null=True)),
                ('happy_summer_rain', models.FloatField(blank=True, null=True)),
                ('happy_spring', models.FloatField(blank=True, null=True)),
                ('happy_spring_rain', models.FloatField(blank=True, null=True)),
                ('sad_spring_rain', models.FloatField(blank=True, null=True)),
                ('sad_spring', models.FloatField(blank=True, null=True)),
                ('sad_summer_rain', models.FloatField(blank=True, null=True)),
                ('sad_summer', models.FloatField(blank=True, null=True)),
                ('sad_fall_rain', models.FloatField(blank=True, null=True)),
                ('sad_fall', models.FloatField(blank=True, null=True)),
                ('sad_winter_rain', models.FloatField(blank=True, null=True)),
                ('sad_winter', models.FloatField(blank=True, null=True)),
                ('sad_winter_snow', models.FloatField(blank=True, null=True)),
                ('angry_winter', models.IntegerField(blank=True, null=True)),
                ('angry_winter_snow', models.IntegerField(blank=True, null=True)),
                ('angry_winter_rain', models.IntegerField(blank=True, null=True)),
                ('angry_fall', models.IntegerField(blank=True, null=True)),
                ('angry_fall_rain', models.IntegerField(blank=True, null=True)),
                ('angry_summer', models.IntegerField(blank=True, null=True)),
                ('angry_summer_rain', models.IntegerField(blank=True, null=True)),
                ('angry_spring', models.IntegerField(blank=True, null=True)),
                ('angry_spring_rain', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'menu_score_all',
                'managed': False,
            },
        ),
    ]
