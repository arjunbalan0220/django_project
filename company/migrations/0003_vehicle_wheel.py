# Generated by Django 5.1.4 on 2025-01-15 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0002_vehicle'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicle',
            name='Wheel',
            field=models.CharField(max_length=5, null=True),
        ),
    ]
