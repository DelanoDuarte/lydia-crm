# Generated by Django 3.2.5 on 2021-07-13 12:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('partner', '0002_auto_20210712_0908'),
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('STARTED', 'STARTED'), ('IN_PROGRESS', 'IN_PROGRESS'), ('PENDING', 'PENDING'), ('COMPLETED', 'COMPLETED')], max_length=128)),
                ('purchaseDate', models.DateTimeField()),
                ('comments', models.CharField(max_length=2048)),
                ('partner', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='partner.partner')),
                ('products', models.ManyToManyField(to='product.Product')),
            ],
        ),
    ]
