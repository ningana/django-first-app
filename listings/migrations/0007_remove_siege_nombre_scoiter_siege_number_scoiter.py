# Generated by Django 4.1 on 2022-08-13 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0006_siege'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='siege',
            name='nombre_scoiter',
        ),
        migrations.AddField(
            model_name='siege',
            name='number_scoiter',
            field=models.IntegerField(default=2),
            preserve_default=False,
        ),
    ]
