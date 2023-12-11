# Generated by Django 4.2.6 on 2023-12-06 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_userrequest_created_at'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userrequest',
            options={'ordering': ['-created_at'], 'verbose_name': 'Заявка', 'verbose_name_plural': 'Заявки'},
        ),
        migrations.AlterField(
            model_name='userrequest',
            name='pinfl',
            field=models.CharField(max_length=14, verbose_name='ПИНФЛ'),
        ),
    ]