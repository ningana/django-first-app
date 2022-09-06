# Generated by Django 4.1 on 2022-08-17 17:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0010_users_alter_siege_genre'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmailPassword',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Email', models.EmailField(max_length=254)),
                ('Password', models.CharField(max_length=30)),
            ],
        ),
        migrations.RemoveField(
            model_name='users',
            name='password',
        ),
        migrations.AlterField(
            model_name='users',
            name='email',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='listings.emailpassword'),
        ),
    ]