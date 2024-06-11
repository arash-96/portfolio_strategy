from django.forms import ModelForm, forms
from .models import Trade

class TradeForm(ModelForm):
    class Meta:
        model = Trade
        fields = [
            'instrumentType','tradeDate', 'securityID', 'comment' , 'strategy', 'strategyID' , 'price' , 'spread',
            'notional', 'direction', 'username'
            ]
        
        labels = {
            'instrumentType': 'Instrument Type',
            'tradeDate': 'Trade Date',  
            'securityID': 'Security ID',
            'comment': 'Comment',
            'strategy': 'Strategy',
            'strategyID': 'Strategy ID',
            'price': 'Price',
            'spread': 'Spread',
            'notional': 'Notional',
            'direction': 'Direction',
            'username': 'Username'
            }       