# Generated by Django 5.0.6 on 2024-06-11 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_alter_trade_tradedate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trade',
            name='notional',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=20),
        ),
        migrations.AlterField(
            model_name='trade',
            name='price',
            field=models.FloatField(blank=True),
        ),
        migrations.AlterField(
            model_name='trade',
            name='spread',
            field=models.FloatField(blank=True),
        ),
    ]
