# Generated by Django 5.0.6 on 2024-06-10 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_alter_trade_numbercontracts'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trade',
            name='tradeDate',
            field=models.DateField(),
        ),
    ]