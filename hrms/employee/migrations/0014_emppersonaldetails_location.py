# Generated by Django 5.0.6 on 2024-10-26 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0013_empsalarydetails_dapayamt_empsalarydetails_pf_type_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='emppersonaldetails',
            name='location',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
