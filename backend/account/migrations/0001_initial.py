# Generated by Django 5.1.3 on 2024-11-20 17:17

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('surname', models.CharField(max_length=255)),
                ('birthday', models.DateField()),
                ('cellphone', models.CharField(blank=True, max_length=255, null=True)),
                ('agree_policy', models.BooleanField()),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('email_notifications', models.BooleanField(default=True)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('last_activity', models.DateTimeField(blank=True, null=True)),
                ('last_password_change', models.DateTimeField(blank=True, null=True)),
                ('last_neighborhood_change', models.DateTimeField(blank=True, null=True)),
                ('muted', models.BooleanField(default=False)),
                ('mute_date', models.DateTimeField(blank=True, null=True)),
                ('mute_days', models.IntegerField(blank=True, null=True)),
                ('mute_count', models.IntegerField(default=0)),
                ('suspension_reason', models.TextField(blank=True, max_length=255, null=True)),
                ('join_date', models.DateTimeField(editable=False)),
                ('update_date', models.DateTimeField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]