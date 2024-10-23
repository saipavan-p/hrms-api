# Generated by Django 5.0.6 on 2024-10-16 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_login_company_login_is_admin_login_is_staff_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='login',
            name='is_company_setup_complete',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='login',
            name='role',
            field=models.CharField(choices=[('admin', 'Admin'), ('employee', 'Employee')], default='employee', max_length=20),
        ),
        migrations.AlterField(
            model_name='login',
            name='password',
            field=models.CharField(max_length=128),
        ),
    ]