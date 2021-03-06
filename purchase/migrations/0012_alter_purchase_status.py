# Generated by Django 3.2.5 on 2021-07-24 16:56

from django.db import migrations, models
import enum


class Migration(migrations.Migration):

    dependencies = [
        ('purchase', '0011_alter_purchase_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='status',
            field=models.CharField(choices=[('STARTED', 'STARTED'), ('IN_PROGRESS', 'IN_PROGRESS'), ('PENDING', 'PENDING'), ('FAILED', 'FAILED'), ('COMPLETED', 'COMPLETED')], default=enum.Enum.__str__, max_length=128),
        ),
    ]
