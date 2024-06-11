from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Trade
from .forms import TradeForm
from collections import Counter
import json

# Create your views here.
def home(request):
    if request.method == 'GET':
        form = TradeForm()
        trades = Trade.objects.all()
        # instrument_types = [trade.instrumentType for trade in trades]
        # instrument_type_counts = Counter(instrument_types)

        # instrument_types = ['Bonds', 'CDS', 'Futures', 'FX']
        # instrument_counts = [0, 0, 0, 0]
        
        #counts = list(instrument_type_counts.values())

        instrument_counts = {
            'Bonds' : 0,
            'CDS' : 0,
            'Futures' : 0,
            'FX' : 0
        }
        for trade in trades:
            instrument_counts[trade.instrumentType] += 1
       
        print(instrument_counts)

        context = {
            'form': form,
            'trades': trades,
            'counts': instrument_counts,
        }
        return render(request, 'home.html', context)
    elif request.method == 'POST':
        form = TradeForm(request.POST)
        if form.is_valid():        
            form.save()        
            return HttpResponseRedirect('')
        else:        
            return HttpResponseRedirect('/error/')
    else:        
        return HttpResponseRedirect('/error/')
