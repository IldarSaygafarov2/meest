# Generated by Django 4.2.6 on 2023-12-06 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_userrequest_options_alter_userrequest_pinfl'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userrequest',
            name='passport_number',
            field=models.CharField(max_length=12, verbose_name='Номер паспорта'),
        ),
    ]