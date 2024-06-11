from django.forms import ModelForm, forms
from .models import Trade

class TradeForm(ModelForm):
    class Meta:
        model = Trade
        fields = [            
            'instrumentType',
            'securityID',
            'username',
            'comment',
            'strategy', 
            'strategyID', 
            'price',
            'spread',
            'notional',
            'direction', 
            'numberContracts',
            'tradeDate'    
            ]
        
        labels = {
            'instrumentType' : 'Instrument Type',
            'securityID' : 'Security ID',
            'username' : 'Username',
            'comment' : 'Comment',
            'strategy' : 'Strategy', 
            'strategyID' : 'StrategyID', 
            'price' : 'Price',
            'spread' : 'Spread',
            'notional' : 'Notional',
            'direction' : 'Direction', 
            'numberContracts' : 'NumberContracts',
            'tradeDate' : 'Trade Date'    
            }       