# Generated by Django 4.1 on 2022-08-17 17:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0012_remove_users_email_emailpassword_proprio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailpassword',
            name='proprio',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='listings.users'),
            preserve_default=False,
        ),
    ]
