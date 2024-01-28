# Generated by Django 5.0.1 on 2024-01-28 11:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommercemain', '0002_user_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('authorized_user_id', models.CharField(blank=True, max_length=255, null=True)),
                ('status', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ecommercemain.status')),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ecommercemain.user')),
            ],
        ),
    ]
