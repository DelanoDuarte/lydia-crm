# Generated by Django 3.2.5 on 2021-07-18 16:30

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('purchase', '0004_alter_purchase_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchase',
            name='createdAt',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
