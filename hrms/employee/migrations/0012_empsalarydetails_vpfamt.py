# Generated by Django 5.0.6 on 2024-10-22 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0011_empworkdetails_company_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='empsalarydetails',
            name='VPFAMT',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
