# Generated by Django 3.0.8 on 2020-07-31 15:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Board', '0002_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='board_num',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Board.Board'),
        ),
    ]
