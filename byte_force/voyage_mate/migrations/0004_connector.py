# Generated by Django 5.1.3 on 2024-11-16 11:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voyage_mate', '0003_city'),
    ]

    operations = [
        migrations.CreateModel(
            name='Connector',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='connectors', to='voyage_mate.city')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='connectors', to='voyage_mate.destination')),
            ],
        ),
    ]
