# Generated by Django 3.2.5 on 2021-08-06 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('purchase', '0028_alter_purchase_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='purchaseDate',
            field=models.DateField(),
        ),
    ]
