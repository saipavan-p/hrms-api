# Generated by Django 5.0.6 on 2024-10-22 11:03

from django.db import migrations

def set_default_voluntary_pf(apps, schema_editor):
    Employee = apps.get_model('payrole', 'EmployeeCompensation')  # Change to your actual model name
    Employee.objects.filter(voluntary_pf__isnull=True).update(voluntary_pf=False)  # Set to False, or True based on your requirement

class Migration(migrations.Migration):

    dependencies = [
        ('payrole', '0022_alter_employeecompensation_voluntary_pf'),
    ]

    operations = [
        migrations.RunPython(set_default_voluntary_pf),
    ]
