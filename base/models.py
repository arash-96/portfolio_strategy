from django.db import models
import uuid

INSTRUMENT_TYPES = (
    ('CDS', 'CDS'),
    ('Bonds', 'Bonds'),
    ('Futures', 'Futures'),
    ('FX', 'FX'),
)


# Create your models here.
class Trade(models.Model):
    timeStamp = models.DateTimeField(auto_now=True)
    tradeID = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    instrumentType = models.CharField(max_length=100, choices=INSTRUMENT_TYPES, default='CDS')
    securityID = models.CharField(max_length=20, unique=True)
    username = models.CharField(max_length=300)
    comment = models.TextField(max_length=800, null=True, blank=True)
    strategy = models.CharField(max_length=300, null=True, blank=True)
    strategyID = models.CharField(max_length=100, null=True, blank=True)
    price = models.FloatField(blank=True)
    spread = models.FloatField(blank=True)
    notional = models.DecimalField(max_digits=20, decimal_places=2, blank=True) 
    direction = models.CharField(max_length=100)
    numberContracts = models.IntegerField(blank=True, null=True)
    tradeDate = models.DateField()

    def __str__(self):
        return self.securityID
