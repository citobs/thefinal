# Generated by Django 4.1.3 on 2022-12-09 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0007_authgroup_authgrouppermissions_authpermission_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='choice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('res', models.CharField(max_length=300, null=True)),
                ('menu', models.CharField(max_length=300, null=True)),
                ('emotion', models.CharField(max_length=300, null=True)),
                ('cr_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('weather', models.CharField(max_length=300, null=True)),
                ('season', models.CharField(max_length=300, null=True)),
            ],
        ),
    ]
