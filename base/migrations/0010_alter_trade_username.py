# Generated by Django 5.0.6 on 2024-06-12 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0009_alter_trade_direction_alter_trade_notional_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trade',
            name='username',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]