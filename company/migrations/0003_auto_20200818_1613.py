# Generated by Django 3.0.9 on 2020-08-18 16:13

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('company', '0002_auto_20200818_1600'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='branch',
            options={'verbose_name': 'Branch',
                     'verbose_name_plural': 'Branches'},
        ),
    ]
