# Generated by Django 4.0.8 on 2023-01-15 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='E-mail')),
                ('is_verified', models.BooleanField(default=False, verbose_name='Verified')),
                ('is_active', models.BooleanField(default=False, verbose_name='Active')),
                ('is_staff', models.BooleanField(default=False, verbose_name='Staff')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]