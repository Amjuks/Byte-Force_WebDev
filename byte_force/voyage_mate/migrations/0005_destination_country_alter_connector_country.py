# Generated by Django 5.1.3 on 2024-11-16 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voyage_mate', '0004_connector'),
    ]

    operations = [
        migrations.AddField(
            model_name='destination',
            name='country',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='connector',
            name='country',
            field=models.CharField(max_length=255),
        ),
    ]
