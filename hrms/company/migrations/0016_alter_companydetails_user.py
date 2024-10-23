# Generated by Django 5.0.6 on 2024-10-20 17:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0015_alter_companydetails_user'),
        ('users', '0008_login_is_payroll_setup_complete'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companydetails',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.login'),
        ),
    ]