# Generated by Django 5.0.6 on 2024-10-29 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payrole', '0028_employeecompensation_hra_enabled'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeecompensation',
            name='hra_percentage',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
