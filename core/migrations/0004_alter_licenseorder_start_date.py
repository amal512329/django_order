# Generated by Django 4.1.7 on 2023-09-14 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_licenseorder_start_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='licenseorder',
            name='start_date',
            field=models.IntegerField(max_length=20),
        ),
    ]
