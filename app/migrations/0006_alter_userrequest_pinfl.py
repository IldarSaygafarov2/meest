# Generated by Django 4.2.6 on 2023-12-27 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_alter_userrequest_pinfl'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userrequest',
            name='pinfl',
            field=models.TextField(verbose_name='ПИНФЛ'),
        ),
    ]
