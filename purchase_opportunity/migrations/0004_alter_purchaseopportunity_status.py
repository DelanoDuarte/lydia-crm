# Generated by Django 3.2.5 on 2021-07-18 16:32

from django.db import migrations, models
import enum


class Migration(migrations.Migration):

    dependencies = [
        ('purchase_opportunity', '0003_alter_purchaseopportunity_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchaseopportunity',
            name='status',
            field=models.CharField(choices=[('NEW', 'NEW'), ('INTERESTED', 'INTERESTED'), ('ON_GOING', 'ON_GOING'), ('CONVERTED', 'CONVERTED'), ('NOT_CONVERTED', 'NOT_CONVERTED')], default=enum.Enum.__str__, max_length=128),
        ),
    ]
