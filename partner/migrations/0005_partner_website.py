# Generated by Django 3.2.5 on 2021-07-22 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('partner', '0004_partner_partnertype'),
    ]

    operations = [
        migrations.AddField(
            model_name='partner',
            name='website',
            field=models.CharField(max_length=512, null=True),
        ),
    ]
