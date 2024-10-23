# Generated by Django 5.0.6 on 2024-10-15 12:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0010_companydetails_is_company_details_completed_and_more'),
        ('users', '0004_remove_login_last_login_alter_login_email_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='login',
            name='company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='company.companydetails'),
        ),
        migrations.AddField(
            model_name='login',
            name='is_admin',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='login',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='login',
            name='last_login',
            field=models.DateTimeField(blank=True, null=True, verbose_name='last login'),
        ),
        migrations.AlterField(
            model_name='login',
            name='password',
            field=models.CharField(max_length=128, verbose_name='password'),
        ),
    ]