# Generated by Django 3.0.8 on 2020-08-20 11:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polioapp', '0002_auto_20200820_2005'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='boardnum',
            new_name='b_boardnum',
        ),
        migrations.RenameField(
            model_name='blog',
            old_name='body',
            new_name='b_body',
        ),
        migrations.RenameField(
            model_name='blog',
            old_name='pub_date',
            new_name='b_pub_date',
        ),
        migrations.RenameField(
            model_name='blog',
            old_name='title',
            new_name='b_title',
        ),
        migrations.RenameField(
            model_name='news',
            old_name='boardnum',
            new_name='n_boardnum',
        ),
        migrations.RenameField(
            model_name='news',
            old_name='body',
            new_name='n_body',
        ),
        migrations.RenameField(
            model_name='news',
            old_name='pub_date',
            new_name='n_pub_date',
        ),
        migrations.RenameField(
            model_name='news',
            old_name='title',
            new_name='n_title',
        ),
    ]
