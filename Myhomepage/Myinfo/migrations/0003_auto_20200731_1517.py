# Generated by Django 3.0.8 on 2020-07-31 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Myinfo', '0002_auto_20200731_1422'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myinfo',
            name='photo',
            field=models.CharField(max_length=500, null='true'),
        ),
    ]
