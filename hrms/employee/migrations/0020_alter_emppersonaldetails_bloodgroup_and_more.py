# Generated by Django 5.0.6 on 2024-11-12 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0019_alter_emppersonaldetails_dob'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emppersonaldetails',
            name='bloodGroup',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='emppersonaldetails',
            name='relationship',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='emppersonaldetails',
            name='relationshipName',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
