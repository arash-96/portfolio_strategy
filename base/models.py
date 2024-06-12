from django.db import models
import uuid

INSTRUMENT_TYPES = (
    ('CDS', 'CDS'),
    ('Bonds', 'Bonds'),
    ('Futures', 'Futures'),
    ('FX', 'FX'),
)

DIRECTION = (
    ('Buy', 'Buy (Short risk)'),
    ('Sell', 'Sell (Long)'),
)

# Create your models here.
class Trade(models.Model):
    timeStamp = models.DateTimeField(auto_now=True)
    tradeID = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    instrumentType = models.CharField(max_length=100, choices=INSTRUMENT_TYPES, default='CDS')
    securityID = models.CharField(max_length=20, unique=True)
    username = models.CharField(max_length=300, null=True, blank=True)
    comment = models.TextField(max_length=800, null=True, blank=True)
    strategy = models.CharField(max_length=300, null=True, blank=True)
    strategyID = models.CharField(max_length=100, null=True, blank=True)
    price = models.FloatField(blank=True, null=True)
    spread = models.FloatField(blank=True, null=True)
    notional = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True) 
    direction = models.CharField(max_length=100, choices=DIRECTION, default='Buy')
    numberContracts = models.IntegerField(blank=True, null=True)
    tradeDate = models.DateField()

    def __str__(self):
        return self.securityID
