# Generated by Django 5.0.6 on 2024-10-17 08:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_login_is_company_setup_complete_login_role_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='login',
            name='is_staff',
        ),
    ]