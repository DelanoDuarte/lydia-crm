# Generated by Django 3.2.5 on 2021-07-13 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('purchase', '0002_alter_purchase_purchasedate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='comments',
            field=models.CharField(max_length=2048, null=True),
        ),
    ]