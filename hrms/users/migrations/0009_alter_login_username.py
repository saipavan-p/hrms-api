# Generated by Django 5.0.6 on 2024-10-25 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_login_is_payroll_setup_complete'),
    ]

    operations = [
        migrations.AlterField(
            model_name='login',
            name='userName',
            field=models.CharField(max_length=150, unique=True),
        ),
    ]
