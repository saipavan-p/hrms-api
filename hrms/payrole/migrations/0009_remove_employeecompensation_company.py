# Generated by Django 5.0.6 on 2024-10-14 06:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payrole', '0008_remove_employeecompensation_gratuity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employeecompensation',
            name='company',
        ),
    ]
