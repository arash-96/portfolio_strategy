# Generated by Django 5.0.6 on 2024-06-10 17:08

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_trade_strategyid_alter_trade_numbercontracts'),
    ]

    operations = [
        migrations.RenameField(
            model_name='trade',
            old_name='securityId',
            new_name='securityID',
        ),
        migrations.RemoveField(
            model_name='trade',
            name='id',
        ),
        migrations.RemoveField(
            model_name='trade',
            name='instrumentType',
        ),
        migrations.RemoveField(
            model_name='trade',
            name='tradeDate',
        ),
        migrations.AddField(
            model_name='trade',
            name='tradeID',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]