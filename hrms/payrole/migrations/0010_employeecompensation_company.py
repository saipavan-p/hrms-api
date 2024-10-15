# Generated by Django 5.0.6 on 2024-10-14 06:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0010_companydetails_is_company_details_completed_and_more'),
        ('payrole', '0009_remove_employeecompensation_company'),
    ]

    operations = [
        migrations.AddField(
            model_name='employeecompensation',
            name='company',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='compensations', to='company.companydetails'),
            preserve_default=False,
        ),
    ]
