# Generated by Django 4.1 on 2022-08-16 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0008_band_siege'),
    ]

    operations = [
        migrations.AlterField(
            model_name='band',
            name='genre',
            field=models.CharField(choices=[('HH', 'Hip Hop'), ('SP', 'Synth Pop'), ('AR', 'Alternative Rock'), ('RG', 'Reague'), ('ZL', 'Zouk Love'), ('DL', 'Gospel')], max_length=5),
        ),
    ]