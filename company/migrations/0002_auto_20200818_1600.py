# Generated by Django 3.0.9 on 2020-08-18 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Branch name')),
                ('facade_image', models.ImageField(null=True, upload_to='uploads/', verbose_name='Facade image')),
                ('longitude', models.FloatField(db_index=True, verbose_name='Longitude')),
                ('latitude', models.FloatField(db_index=True, verbose_name='Latitude')),
            ],
        )
    ]
