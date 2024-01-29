# Generated by Django 5.0.1 on 2024-01-29 06:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommercemain', '0006_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color_title', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size_title', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=100)),
                ('stock_in_hand', models.PositiveIntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('description', models.TextField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecommercemain.category')),
                ('color', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecommercemain.color')),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecommercemain.seller')),
                ('status', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ecommercemain.status')),
                ('size', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecommercemain.size')),
            ],
        ),
    ]