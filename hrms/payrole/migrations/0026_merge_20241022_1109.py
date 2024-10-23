
# Generated by Django 5.0.6 on 2024-10-22 11:07

from django.db import migrations

def fix_voluntary_pf_values(apps, schema_editor):
    Employee = apps.get_model('payrole', 'EmployeeCompensation')  # Update with your actual model name
    Employee.objects.filter(voluntary_pf="").update(voluntary_pf=False)
    Employee.objects.filter(voluntary_pf__isnull=True).update(voluntary_pf=False)

class Migration(migrations.Migration):

    dependencies = [
        ('payrole', '0023_auto_20241022_1103'),
        ('payrole', '0024_auto_20241022_1106'),
        ('payrole', '0025_merge_0023_auto_20241022_1103_0024_auto_20241022_1106'),
    ]

    operations = [
        migrations.RunPython(fix_voluntary_pf_values),
    ]