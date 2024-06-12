from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from .models import Trade
from .forms import TradeForm
import json

# Create your views here.
def home(request):
    if request.method == 'GET':
        form = TradeForm()
        trades = Trade.objects.all()       

        instrument_counts = {
            'Bonds' : 0,
            'CDS' : 0,
            'Futures' : 0,
            'FX' : 0
        }
        for trade in trades:
            instrument_counts[trade.instrumentType] += 1

        context = {
            'form': form,
            'trades': trades,
            'counts': instrument_counts,
        }
        return render(request, 'home.html', context)
    elif request.method == 'POST':        
        form = TradeForm(request.POST)        
        print(form.errors)     
        if form.is_valid():        
            form.save()        
            return HttpResponseRedirect('')
        else:        
            return HttpResponseRedirect('/error/')
    else:        
        return HttpResponseRedirect('/error/')
    

def new_trade(request, pk):
    trade = get_object_or_404(Trade, tradeID=pk)

    if request.method == 'POST':
        data = json.loads(request.body)
        
        for field_name, field_value in data.items():
            print(field_name, field_value)
            if hasattr(trade, field_name):
                if field_value != 'None':  
                    setattr(trade, field_name, field_value)
                else:                
                    print(f'Field "{field_name}" value is None for Trade ID {pk}. Skipping update.')
            else:
                #print(f'Field "{field_name}" does not exist for Trade ID {pk}')
                return JsonResponse({'success': False, 'error': 'Invalid field(s) provided'})
        
        trade.save()
        return JsonResponse({'success': True})
    else:
        return JsonResponse({'success': False, 'error': 'Invalid request method'})
