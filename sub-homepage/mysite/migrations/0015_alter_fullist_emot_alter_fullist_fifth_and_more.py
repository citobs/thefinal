# Generated by Django 4.0.8 on 2022-12-08 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0014_fullist_wea'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fullist',
            name='emot',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='fullist',
            name='fifth',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='fullist',
            name='first',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='fullist',
            name='fourth',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='fullist',
            name='sea',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='fullist',
            name='second',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='fullist',
            name='third',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='fullist',
            name='wea',
            field=models.CharField(max_length=300, null=True),
        ),
    ]
