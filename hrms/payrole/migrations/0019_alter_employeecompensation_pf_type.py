# Generated by Django 5.0.6 on 2024-10-22 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payrole', '0018_alter_employeecompensation_pf_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeecompensation',
            name='pf_type',
            field=models.CharField(blank=True, choices=[('>15k', 'Greater than 15k'), ('<=15k', 'Less than or equal to 15k'), ('Both1', 'Both6')], max_length=10, null=True),
        ),
    ]