# Generated by Django 5.0.6 on 2024-11-04 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0016_alter_emppersonaldetails_educationalqualification'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empsocialsecuritydetails',
            name='aadharNum',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='empsocialsecuritydetails',
            name='bankAccountNumber',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='empsocialsecuritydetails',
            name='bankName',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='empsocialsecuritydetails',
            name='ifscCode',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='empsocialsecuritydetails',
            name='panNum',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='empsocialsecuritydetails',
            name='uanNum',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]